import json


def hello(event, context):
    body = {
        "message": {
            "helloworld" : "this is the new api"
        }
    }

    response = {
        "statusCode": 200,
        "headers": {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "*"
        },
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
