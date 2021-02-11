import boto3
def initilizeBoto(clientName):
    boto3.client(clientName)

def createApplication():
    client = initilizeBoto("example")
    response = client.create_application(
        Name='string',
        Description='string',
        Tags={
            'string': 'string'
        }
    )
    return response

def createConfigFile():
    client = initilizeBoto("example")
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