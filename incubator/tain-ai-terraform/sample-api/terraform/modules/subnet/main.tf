resource "aws_subnet" "subnet" {
  count = length(var.cidrs)

  vpc_id            = var.vpc_id
  cidr_block        = var.cidrs[count.index]
  availability_zone = var.availability_zones[count.index]

  tags = {
    Name = "${var.name}_${var.availability_zones[count.index]}"
  }
}

resource "aws_route_table" "subnet" {
  count = length(var.cidrs)

  vpc_id = var.vpc_id

  tags = {
    Name = "${var.name}_${var.availability_zones[count.index]}"
  }
}

resource "aws_route_table_association" "subnet" {
  count = length(var.cidrs)

  subnet_id      = aws_subnet.subnet[count.index].id
  route_table_id = aws_route_table.subnet[count.index].id
}
