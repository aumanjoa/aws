#!/bin/sh

eksctl create cluster \                                                                                               ✔  3173  21:41:23
> --name k8s \
> --version 1.14 \
> --region eu-central-1 \
> --nodegroup-name standard-workers \
> --node-type t2.micro \
> --nodes 2 \
> --nodes-min 1 \
> --nodes-max 2 \
> --node-ami auto


kubectl apply -f rbac.yaml

helm init --service-account tiller

helm repo update

helm repo add bitnami https://charts.bitnami.com/bitnami

helm install --name my-release stable/nginx-ingress

eksctl scale nodegroup --cluster=k8s --nodes=4 --name=standard-workers
