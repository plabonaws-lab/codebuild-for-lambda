import json

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!. Just Now Completed CI/CD using Github & Lambda, Code will Change automatically')
    }
