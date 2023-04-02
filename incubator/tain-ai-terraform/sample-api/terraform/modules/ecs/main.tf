locals {
  host_port      = 3000
  container_port = 3000
}

module "lb" {
  source = "../lb"

  name    = var.name
  vpc_id  = var.vpc_id
  subnets = var.public_subnet_ids
}

resource "aws_security_group" "ecs" {
  name   = "${var.name}-ecs"
  vpc_id = var.vpc_id

  ingress {
    from_port   = local.host_port
    to_port     = local.container_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_ecs_cluster" "ecs" {
  name = var.name
}

resource "aws_ecs_service" "ecs" {
  name            = var.name
  cluster         = aws_ecs_cluster.ecs.id
  task_definition = aws_ecs_task_definition.ecs.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = var.private_subnet_ids
    security_groups  = [aws_security_group.ecs.id]
    assign_public_ip = false
  }

  load_balancer {
    target_group_arn = module.lb.target_gropu_arn
    container_name   = var.name
    container_port   = local.container_port
  }

  depends_on = [module.lb, aws_iam_role_policy_attachment.ecs_task_execution_role]
}
