import requests

def get_data() -> dict:
    response = requests.get('https://api.github.com/events')

    return response.json()


def lambda_handler(event, context):
    data = get_data()

    return {
        'statusCode': 200,
        'body': data
    }
