#!/bin/bash
#cli command to find and remove delete markers.  
#https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-objects-versioned-bucket.html
PROFILE=s3
REGION=us-west-2
BUCKET=$1
aws --profile $PROFILE s3api delete-objects \
    --region $REGION \
    --bucket $BUCKET \
    --delete "$(aws --profile $PROFILE s3api list-object-versions \
                    --region $REGION \
                    --bucket $BUCKET \
                    --output=json \
                    --query='{Objects: DeleteMarkers[].{Key:Key,VersionId:VersionId}}')"
