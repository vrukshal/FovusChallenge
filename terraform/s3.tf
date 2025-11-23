# S3 bucket
resource "aws_s3_bucket" "upload_bucket" {
  bucket = "s3-upload-bucket-demo"
}
