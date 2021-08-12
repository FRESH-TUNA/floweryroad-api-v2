#!/bin/sh

aws eks --region ap-northeast-2 update-kubeconfig --name floweryroad

kubectl create namespace floweryroad

kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v1.0.2/cert-manager.yaml 

kubectl apply -f ingress_base.yaml

# 조금 기다리고 해야 한다.
kubectl apply -f ingress.yaml

kubectl create secret generic app --from-env-file=../.envs/staging/app.env -n floweryroad
kubectl create secret generic auth --from-env-file=../.envs/staging/auth.env -n floweryroad

export TAG=1.0.0
envsubst < ../app.yaml | kubectl apply -f -
envsubst < ../auth.yaml | kubectl apply -f -
