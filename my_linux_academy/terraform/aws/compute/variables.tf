#-------compute/variables.tf---------
variable "public_key_path" {
  default = #add something
}

variable "key_name" {
  default = "tfkey"
}

variable "subnet_ips" {
  type = "list"
}

variable "instance_count" {}

variable "instance_type" {}

variable "security_group" {}

variable "subnets" {
  type = "list"
}
