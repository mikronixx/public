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
