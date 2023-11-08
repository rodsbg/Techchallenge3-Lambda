import json
import requests

def lambda_handler(event, context):
    try:
        # Pretty-print the entire event object
        print("Event Object Details:")

        path_value = event.get("path")
        print(path_value)

        # Construct the API URL
        api_url = f'http://a019d4cd505734764902a37394dcd127-1458754499.us-east-1.elb.amazonaws.com:3000/api/{path_value}'
        print(f"API URL: {api_url}")

        # Set the headers for the HTTP request
        headers = {'Content-Type': 'application/json'}

        # Send an HTTP POST request with the event data
        response = requests.post(api_url, json=event, headers=headers)

        # Check if the request was successful
        response.raise_for_status()

        # Extract the JSON response from the API
        response_data = response.json()

        print(f"API Response: {response_data}")

        return {
            "statusCode": response.status_code,
            "body": json.dumps(response_data)
        }
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Request error: {str(e)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f'Unhandled error: {str(e)}'})
        }
