#https://boto3.amazonaws.com/v1/documentation/api/latest/index.html 
import boto3

#basic boto3 auth using local aws credentials 
def boto3session():
    boto3session=boto3.Session(
    region_name="us-west-2")
    return boto3session
boto3session=boto3session()

#create a client that returns a paginated object, which is easier to parse than a dict. 
#boto3 pagination, and why it is cool.  
#aws ec2 describe-instances <args, incl --instance-id> are your friends here

def ec2instances(boto3session):
    ec2instances=[]
    pagination_filters = [{
        'Name': 'instance-state-name',
        'Values': ['running']}]
    page = boto3session.client('ec2').get_paginator('describe_instances').paginate(Filters=pagination_filters).build_full_result()
    for reservation in page['Reservations']:
        for instance in reservation['Instances']:
            ec2instances.append([instance['InstanceId'],instance['PublicIpAddress'], instance['PrivateIpAddress']])  
    return ec2instances

print(ec2instances(boto3session))

