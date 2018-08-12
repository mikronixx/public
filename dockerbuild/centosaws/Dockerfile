FROM centos:latest
MAINTAINER mikron@frieswiththat.org
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm && yum -y update && yum -y install epel-release python36u bash python36u-pip  python36u-setuptools
RUN pip3.6 install awscli requests boto3
ENTRYPOINT ["aws"]

