terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_dynamodb_table" "basic_dynamodb_table" {
  name           = "DynamoDB-Terraform"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity  = 20
  hash_key       = "UserId"
  range_key      = "Name"

  attribute {
    name = "UserId"
    type = "S"
  }

  attribute {
    name = "Name"
    type = "S"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  global_secondary_index {
    name               = "UserTitleIndex"
    hash_key           = "UserId"
    range_key          = "Name"
    write_capacity     = 10
    read_capacity      = 10
    projection_type    = "KEYS_ONLY"
    non_key_attributes = []
  }

  tags = {
    Name        = "dynamodb-table"
    Environment = "Training"
  }
}
