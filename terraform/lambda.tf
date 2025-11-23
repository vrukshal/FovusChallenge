# Lambda function
resource "aws_lambda_function" "s3_to_dynamo" {
  function_name = "s3_to_dynamo"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.12"
  role          = aws_iam_role.lambda_role.arn
  filename      = "lambda.zip" # ZIP containing your code
}
