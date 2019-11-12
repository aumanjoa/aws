#!/bin/sh

aws s3 mb s3://joachim-hello-aws

aws s3 cp index.html s3://joachim-hello-aws

aws s3api put-object-acl --bucket joachim-hello-aws --key index.html --acl public-read

#https://joachim-hello-aws.s3.eu-central-1.amazonaws.com/index.html

aws cloudfront create-distribution \
  --origin-domain-name joachim-hello-aws.s3.eu-central-1.amazonaws.com \
  --default-root-object index.html

#https://d2q47f3428j8u0.cloudfront.net/