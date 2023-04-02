provider "aws" {
  region     = var.region
  access_key = var.access_key
  secret_key = var.secret_key
}

data "aws_caller_identity" "current" {}

data "aws_availability_zones" "available" {
  state = "available"
}

locals {
  az_list = data.aws_availability_zones.available.names
}

module "network" {
  source = "../../modules/network"

  name                 = var.name
  availability_zones   = [local.az_list[0], local.az_list[2]]
  vpc_cidr             = "10.10.0.0/16"
  private_subnet_cidrs = ["10.10.0.0/24", "10.10.10.0/24"]
  public_subnet_cidrs  = ["10.10.1.0/24", "10.10.11.0/24"]
}

module "ecr" {
  source = "../../modules/ecr"

  name = var.name
}

module "ecs" {
  source = "../../modules/ecs"

  name               = var.name
  region             = var.region
  account_id         = data.aws_caller_identity.current.account_id
  vpc_id             = module.network.vpc_id
  private_subnet_ids = module.network.private_subnet_ids
  public_subnet_ids  = module.network.public_subnet_ids
  repository_url     = module.ecr.repository_url
  secrets = {
    "OREURAK_FIREBASE_SERVICE_ACCOUNT_KEY" = "/prod/firestore/service-account-key"
    "FILM_FIREBASE_SERVICE_ACCOUNT_KEY"    = "/prod/film/firebase/service-account-key"
    "JWT_SECRET_KEY"                       = "/prod/film/jwt-secret-key"
    "OPENAI_API_KEY"                       = "/dev/openai/api-key"
  }
}
