variable "name" {
  type = string
}

variable "subnet_ids" {
  type        = list(string)
  description = "Subnet IDs to use"
}
