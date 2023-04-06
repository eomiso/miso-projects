variable "region" {
  type        = string
  description = "AWS region"
}

variable "account_id" {
  type        = string
  description = "AWS account ID"
}

variable "name" {
  type        = string
  description = "Name of the ECS cluster"
}

variable "vpc_id" {
  type        = string
  description = "VPC ID"
}

variable "private_subnet_ids" {
  type        = list(string)
  description = "Private subnet IDs"
}

variable "public_subnet_ids" {
  type        = list(string)
  description = "Public subnet IDs"
}

variable "repository_url" {
  type        = string
  description = "ECR repository URL"
}

variable "secrets" {
  type        = map(string)
  description = "Secrets to be passed to the container"
  default     = {}
}

variable "tags" {
  Name = "sample-api"
}
