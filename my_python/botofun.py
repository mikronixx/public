#!/usr/bin/env /usr/bin/python
import boto3
import argparse

parser = argparse.ArgumentParser (description='boto3 test plaform for s3')
parser.add_argument('mybucket',   help='s3 bucket ')
parser.add_argument('myprofile', help='AWS profile')
args = parser.parse_args()
print args.myprofile

boto3.setup_default_session(profile_name=args.myprofile)
s3 = boto3.resource('s3')
bucket = s3.Bucket(args.mybucket)
for obj in bucket.objects.all():
    print(obj.key)

#client = boto3.client('s3')
#response = client.list_buckets()
#x = response.items()
#for a in x:
# print (a)
# print 
