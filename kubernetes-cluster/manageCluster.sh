#!/bin/sh

eksctl create cluster \
--name k8s \
--version 1.14 \
--region us-west-2 \
--nodegroup-name standard-workers \
--node-type t2.micro \
--nodes 2 \
--nodes-min 1 \
--nodes-max 3 \
--node-ami auto