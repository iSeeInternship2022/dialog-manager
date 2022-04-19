import json


def hello(event, context):
    body = {
        "message": '🚀 Hello iSee 👋 ! From Python Here! nds',
        "input": "Hello from iSee Team"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
