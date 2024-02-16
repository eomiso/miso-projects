AWS_ACCESS_KEY_ID = "{{ AWS_ACCESS_KEY_ID }}"
AWS_SECRET_ACCESS_KEY = "{{ AWS_SECRET_ACCESS_KEY }}"
AWS_ROLE_TO_ASSUME = "arn:aws:iam::226685225888:role/SampleApiPushRole"

import boto3

aws_access_key_id = "{{ AWS_ACCESS_KEY_ID }}"
aws_secret_access_key = "{{ AWS_SECRET_ACCESS_KEY }}"

client = boto3.client(
    "sts",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

response = client.assume_role(
    RoleArn=AWS_ROLE_TO_ASSUME, RoleSessionName="SampleApiPushRole"
)

print(
    response["Credentials"]["AccessKeyId"], response["Credentials"]["SecretAccessKey"]
)
