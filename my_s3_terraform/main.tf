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
    id = "production"
   enabled = "true"

   prefix ="*"
   tags {
      "rule" = "age"
      "autoclean" = "true"
         }

   transition {
       storage_class = "STANDARD_IA"
       days = 30
    }

   transition {
       storage_class = "GLACIER"
       days = 90
    }
    }
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
