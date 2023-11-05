import json
import boto3
import os

USER_POOL_ID = 'app-fiap-pos-tech'  # Essa variável não é necessária para initiate_auth
CLIENT_ID = os.getenv('CLIENT_ID', '3i5a4kdna3kj442v67gpk2au82')  # Agora carregando de uma variável de ambiente

client = boto3.client('cognito-idp')

def lambda_handler(event, context):
    try:
    

        #body = json.loads(event.get('body', '{}'))
        #username = body.get('usuario')
        #password = body.get('senha')
      

        username = event['username']
        password = event['password']
       
       
        if not username or not password:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Usuário ou senha não fornecidos no corpo da requisição'})
            }

        response = client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            },
            ClientId=CLIENT_ID
        )
        
      
        return {
            'statusCode': 200,
            'body': json.dumps({
                'AuthenticationResult': response['AuthenticationResult']
            })
        }

    except client.exceptions.NotAuthorizedException:
        return {
            'statusCode': 401,
            'body': json.dumps({'error': 'Usuário ou senha inválidos'})
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Formato de JSON inválido no corpo da requisição'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
