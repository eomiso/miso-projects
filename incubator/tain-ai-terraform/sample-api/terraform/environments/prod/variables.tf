variable "region" {
  type        = string
  description = "The AWS region to deploy into."
  default     = "ap-northeast-2"
}

variable "access_key" {
  type        = string
  description = "The AWS access key to use for Terraform operations."
}

variable "secret_key" {
  type        = string
  description = "The AWS secret key to use for Terraform operations."
}

variable "name" {
  type        = string
  description = "Name of the service"
  default     = "film-server-prod"
}
