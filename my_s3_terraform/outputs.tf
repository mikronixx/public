#-----outputs.tf
output "prod_s3_bucket_name" {
    value = "${aws_s3_bucket.org-frieswiththat.bucket}"
}
output "prod_s3_lifecycle_rule" {
    value = "${aws_s3_bucket.org-frieswiththat.lifecycle_rule}"
}

