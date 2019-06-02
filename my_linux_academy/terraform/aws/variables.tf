variable "project_name" {}
variable "aws_region" {}
variable "aws_credentials" {}

#--------storage variables
variable "profile" {}

#-------networking variables
variable "vpc_cidr" {}

variable "public_cidrs" {
  type = "list"
}

variable "accessip" {}

#-------compute variables
variable "key_name" {}

variable "public_key_path" {}
variable "server_instance_type" {}

variable "instance_count" {
  default = 1
}
