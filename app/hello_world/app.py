import json
import hello

def lambda_handler(event, context):
    # Pure lambda function

    message = hello.create_message()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message
        }),
    }