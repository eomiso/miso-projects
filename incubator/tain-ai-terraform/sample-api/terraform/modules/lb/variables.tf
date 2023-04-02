variable "name" {
  type        = string
  description = "Name of the load balancer"
}

variable "vpc_id" {
  type        = string
  description = "VPC ID to place the load balancer in"
}

variable "subnets" {
  type        = list(string)
  description = "List of subnets to place the load balancer in"
}
