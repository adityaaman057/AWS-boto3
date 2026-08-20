import boto3

iam = boto3.client('iam')

response = iam.delete_user(
    UserName='aman_new'
)

print(response)