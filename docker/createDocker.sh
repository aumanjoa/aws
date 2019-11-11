#!/bin/sh

docker build -t aws-hello .

#docker run --name aws-hello-container -d -p 80:80 aws-hello

docker tag aws-hello aumanjoa/aws-hello

docker push aumanjoa/aws-hello
