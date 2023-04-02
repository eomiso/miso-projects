variable "name" {
  type        = string
  description = "Name of the network"
}

variable "vpc_cidr" {
  type        = string
  description = "CIDR of the VPC"
}

variable "availability_zones" {
  type        = list(string)
  description = "Availability zones to use"
}

variable "private_subnet_cidrs" {
  type        = list(string)
  description = "CIDRs of the private subnets"
}

variable "public_subnet_cidrs" {
  type        = list(string)
  description = "CIDRs of the public subnets"
}
