import json
import boto3

def lambda_handler(event, context):
    source_client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='', region_name='us-east-1')
    source_response = source_client.get_object(Bucket='source-bucket-name',Key='source-object.zip')
    destination_client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='', region_name='us-east-1')
    destination_client.upload_fileobj(source_response['Body'],'destination-bucket-name','destination-filename.zip')
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully copied file!')
    }

