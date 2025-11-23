# DynamoDB table
resource "aws_dynamodb_table" "file_metadata" {
  name         = "file_metadata"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "file_name"

  attribute {
    name = "file_name"
    type = "S"
  }
}
