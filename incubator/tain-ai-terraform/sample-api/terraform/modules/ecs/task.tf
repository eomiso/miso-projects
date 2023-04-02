resource "aws_iam_role" "ecs_task_execution_role" {
  name = "${var.name}-ecs-task-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"

    Statement = [{
      sid    = "1"
      effect = "Allow"
      Action = "sts:AssumeRole"

      Principal = {
        Service = ["ecs-tasks.amazonaws.com"]
      }
    }]
  })

  inline_policy {
    name = "access-parameter-store-role"

    policy = jsonencode({
      Version = "2012-10-17"

      Statement = [{
        Sid    = "1"
        Effect = "Allow"
        Action = [
          "ssm:GetParameters",
          "kms:Decrypt"
        ]
        Resource = concat([for val in var.secrets :
          "arn:aws:ssm:${var.region}:${var.account_id}:parameter${val}"
          ], [
          "arn:aws:kms:ap-northeast-2:075389491675:key/0c06ba75-56fd-40e9-be19-d915fe8c3e58"
        ])
      }]
    })
  }
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_ecs_task_definition" "ecs" {
  family                   = var.name
  cpu                      = 512
  memory                   = 1024
  network_mode             = "awsvpc"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  requires_compatibilities = ["FARGATE"]

  container_definitions = jsonencode([
    {
      name      = var.name
      image     = "${var.repository_url}:latest"
      essential = true

      secrets = [
        for key, value in var.secrets : {
          name      = key
          valueFrom = value
        }
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          "awslogs-group"         = aws_cloudwatch_log_group.log_group.id
          "awslogs-region"        = var.region
          "awslogs-stream-prefix" = "ecs"
        }
      },

      portMappings = [
        {
          containerPort = local.container_port
          hostPort      = local.host_port
          protocol      = "tcp"
        },
      ],
      networkMode : "awsvpc"
    },
  ])
}

