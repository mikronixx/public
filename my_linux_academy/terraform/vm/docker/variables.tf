variable "env" {
   description = "env: dev or prod"
}

variable "image" {
    description = "image for container"
    type = "map"
}

variable "int_port" {
    description = "internal container  port"
    type = "map"
}

variable "ext_port" {
    description = "external container  port"
    type = "map"
}

variable "container_name" {
    description = "container_name"
    type = "map"
}
