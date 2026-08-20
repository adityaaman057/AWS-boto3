import boto3

# Create IAM client
iam = boto3.client('iam')

# Update a user name
response = iam.update_user(
    UserName='aman',
    NewUserName='aman_new'
)

print(response)