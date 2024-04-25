#https://boto3.amazonaws.com/v1/documentation/api/latest/index.html 
import boto3

#basic boto3 auth using local aws credentials 
def boto3session():
    session=boto3.Session(
    region_name="us-west-2",
    profile_name="default")
    return session
print(session)
    
#use it in an ec2 client to describe images 

def findimages(session):
    page=session.client(ec2).getpaginator('describe_images').paginate.build_full_result()