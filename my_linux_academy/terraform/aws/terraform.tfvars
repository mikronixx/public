#------terraform.tfvars
aws_region = "us-west-2"
aws_credentials = #add something
profile = "terraform"
#------storage
project_name = "la-terraform"



#------networking
vpc_cidr = "10.123.0.0/16"
public_cidrs = [
  "10.123.1.0/24",
  "10.123.2.0/24"
  ]
accessip = "0.0.0.0/0"

#------compute
key_name = "id_la"
public_key_path = #add something
server_instance_type = "t2.micro"
instance_count = 2
