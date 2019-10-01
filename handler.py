import json
import boto3

def sendMessages(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    sns = boto3.client("sns")

    body_object = json.loads(event["body"])
    if "sms" in body_object:
        for message in body_object["sms"]:
            print(message)
            sns.publish(
                PhoneNumber=message["number"],
                Message=message["message"],
                Subject=message["subject"],
                MessageAttributes = {
                    'AWS.SNS.SMS.SMSType': {
                        'DataType': 'String',
                        'StringValue': 'Promotional'  # or 'Transactional'
                        }
                }
            )

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    print(json.dumps(event))
    return response