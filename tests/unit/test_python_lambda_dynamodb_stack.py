import aws_cdk as core
import aws_cdk.assertions as assertions

from python_lambda_dynamodb.python_lambda_dynamodb_stack import PythonLambdaDynamodbStack

# example tests. To run these tests, uncomment this file along with the example
# resource in python_lambda_dynamodb/python_lambda_dynamodb_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PythonLambdaDynamodbStack(app, "python-lambda-dynamodb")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
