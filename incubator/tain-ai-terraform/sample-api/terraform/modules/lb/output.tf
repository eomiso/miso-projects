output "target_group_arn" {
  value = aws_lb_target_group.lb.arn
}

output "security_group_id" {
  value = aws_security_group.lb.id
}

output "load_balancer_dns_name" {
  value = aws_lb.lb.dns_name
}
