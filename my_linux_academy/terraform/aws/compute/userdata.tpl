#!/bin/bash
yum install -y httpd
echo "Subnet for firewall: ${firewall_subnets}" >> /var/www/html/index.html
service httpd start
chkconfig httpd on

