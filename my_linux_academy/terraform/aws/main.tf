provider "aws" {
  region                  = "${var.aws_region}"
  shared_credentials_file = "${var.aws_credentials}"
  profile                 = "${var.profile}"
}

terraform {
  backend "s3" {
    bucket = #add here
    key = "terraform/terraform.tfstate"
    region = "us-west-2"
    profile = "terraform"
    shared_credentials_file = #add here
  }
}

#Deploy storage
module "storage" {
  source       = "./storage"
  project_name = "${var.project_name}"
}

#deploy networking
module "networking" {
  source       = "./networking"
  vpc_cidr     = "${var.vpc_cidr}"
  public_cidrs = "${var.public_cidrs}"
  accessip     = "${var.accessip}"
}

#deploy compute
module "compute" {
  source          = "./compute"
  instance_count  = "${var.instance_count}"
  key_name        = "${var.key_name}"
  public_key_path = "${var.public_key_path}"
  instance_type   = "${var.server_instance_type}"
  subnets         = "${module.networking.public_subnets}"
  security_group  = "${module.networking.public_sg}"
  subnet_ips      = "${module.networking.subnet_ips}"
}
