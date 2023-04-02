variable "name" {
  type        = string
  description = "Name of the subnet"
}

variable "vpc_id" {
  type        = string
  description = "VPC ID"
}

variable "cidrs" {
  type        = list(string)
  description = "List of cidrs, for every availability zone you want you need one. Example: 10.0.0.0/24 and 10.0.1.0/24"
}

variable "availability_zones" {
  type        = list(string)
  description = "List of availability zones, for every availability zone you want you need one. Example: us-east-1a and us-east-1b"
}
