# This configures aws – required in all terraform files
provider "aws" {
  region                  = "${var.aws_region}"
  shared_credentials_file = "${var.aws_credentials}"
  profile                 = "${var.profile}"
}
 
resource "aws_s3_bucket"  "org-frieswiththat" {
  bucket = "org.frieswiththat"
  acl    = "private"
  tags {
    Name        = "org.frieswiththat"
    Environment = "Prod"
  }
  versioning {
    enabled = false
  }
  lifecycle_rule {
    id = "age"
   enabled = "false" #was true
   prefix ="*"
   tags {
      "rule" = "age"
      "autoclean" = "true"
         }
   transition {
       storage_class = "ONEZONE_IA"
    }
  }
#   noncurrent_version_expiration {
#       days = 15
#    }
  }
 
resource "aws_s3_bucket"  "org-frieswiththat-test" {
  bucket = "org.frieswiththat.test"
  acl    = "private"
  tags {
    Name        = "org.frieswiththat.test"
    Environment = "Dev"
  }
  versioning {
    enabled = false
  }
}
