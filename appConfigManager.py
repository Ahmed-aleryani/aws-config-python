import logging

import boto3
from botocore.exceptions import ClientError
region="us-east-2"
client = boto3.client("appconfig")
s3 = boto3.resource('s3') #used with put object and Bucket and also get all buckets
# s3 = boto3.client('s3',region_name=region)

def createApplication():
    response = client.create_application(
        Name='Test from python 2',
        Description='this is nothing',
        # Tags={
        #     'string': 'string'
        # }
    )
    return response

def createConfigFile():
    response = client.create_configuration_profile(
        ApplicationId='someId will be here',
        Name='string',
        Description='string',
        LocationUri='string',
        RetrievalRoleArn='string',
        Validators=[
            {
                'Type': 'JSON_SCHEMA'|'LAMBDA',
                'Content': 'string'
            },
        ],
        Tags={
            'string': 'string'
        }
    )
    return response
# print(client)
# for bucket in s3.buckets.all():
#     print(bucket.name)



#I created bucket on the aws using the following code inisde try statements
# try:
#     location = {'LocationConstraint':region}
#     s3.create_bucket(Bucket="ahmed-bucket-app-config",CreateBucketConfiguration=location)
# except ClientError as e:
#     logging.error(e)

data=open("appConfigManager.py","rb")
s3.Bucket("ahmed-bucket-app-config").put_object(Key="appConfigManager.py",Body=data)# I uploaded the file I am using now using this line of code

# print(createApplication())