FROM alpine:latest
MAINTAINER mikron@frieswiththat.org
LABEL version="1.0"
RUN apk add python2 py2-pip bash && pip install awscli boto3 requests
ENTRYPOINT ["aws"]
