from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_dynamodb,
    aws_lambda,
)
from constructs import Construct

class PythonLambdaDynamodbStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        employees_table = aws_dynamodb.Table(
            self, "employees",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        producer_lambda = aws_lambda.Function(self, "create_employee",
                                              runtime=aws_lambda.Runtime.PYTHON_3_6,
                                              handler="create_employee.lambda_handler",
                                              code=aws_lambda.Code.from_asset("./lambda"))

        producer_lambda.add_environment("TABLE_NAME", employees_table.table_name)

        employees_table.grant_write_data(producer_lambda)