
module "vpc" {
  source = "../vpc"

  name = "${var.name}-vpc"
  cidr = var.vpc_cidr
}

module "private_subnet" {
  source = "../subnet"

  name               = "${var.name}-private-subnet"
  vpc_id             = module.vpc.id
  cidrs              = var.private_subnet_cidrs
  availability_zones = var.availability_zones
}

module "public_subnet" {
  source = "../subnet"

  name               = "${var.name}-public-subnet"
  vpc_id             = module.vpc.id
  cidrs              = var.public_subnet_cidrs
  availability_zones = var.availability_zones
}

module "nat" {
  source = "../nat"

  name       = "${var.name}-nat"
  subnet_ids = module.public_subnet.ids
}

resource "aws_route" "public_igw_route" {
  count = length(module.public_subnet.route_table_ids)

  gateway_id             = module.vpc.igw
  route_table_id         = module.public_subnet.route_table_ids[count.index]
  destination_cidr_block = "0.0.0.0/0"
}

resource "aws_route" "private_nat_route" {
  count = length(module.private_subnet.route_table_ids)

  nat_gateway_id         = module.nat.ids[count.index]
  route_table_id         = module.private_subnet.route_table_ids[count.index]
  destination_cidr_block = "0.0.0.0/0"
}

# NAT 게이트웨이를 생성하는데 오래 걸리는데 NAT에 디펜던시가 걸리는 리소스들이 있음
# 따라서 NAT 생성이 안료되기까지 기다리는 설정
# https://github.com/hashicorp/terraform/issues/1178#issuecomment-207369534

resource "null_resource" "dummy_dependency" {
  depends_on = [module.nat]
}
