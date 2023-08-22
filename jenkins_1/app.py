import boto3

s3 = boto3.client('s3')
bucket_name = 'testbucketforfilefromec2'
file_key = 'hello-world.txt'

response = s3.get_object(Bucket=bucket_name, Key=file_key)
content = response['Body'].read().decode('utf-8')

print(content)
