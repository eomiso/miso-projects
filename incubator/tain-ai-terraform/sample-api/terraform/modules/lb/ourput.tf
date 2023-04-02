output "target_gropu_arn" {
  value = aws_lb_target_group.lb.arn
}

output "security_group_id" {
  value = aws_security_group.lb.id
}
