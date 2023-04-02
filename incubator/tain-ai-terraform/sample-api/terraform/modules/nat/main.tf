resource "aws_eip" "nat" {
  count = length(var.subnet_ids)
  vpc   = true

  tags = {
    Name = "${var.name}-${var.subnet_ids[count.index]}"
  }
}

resource "aws_nat_gateway" "nat" {
  count = length(var.subnet_ids)

  allocation_id = aws_eip.nat[count.index].id
  subnet_id     = var.subnet_ids[count.index]

  tags = {
    Name = "${var.name}-${var.subnet_ids[count.index]}"
  }
}
