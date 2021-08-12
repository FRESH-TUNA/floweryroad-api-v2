# 자주 사용하는 명령어 예시

## namespace 생성
```
kubectl create namespace floweryroad
```
## secret 생성
```
kubectl create secret generic app --from-env-file=.envs/staging/app.env -n floweryroad
kubectl create secret generic auth --from-env-file=.envs/staging/auth.env -n floweryroad
```
## secret 제거
```
kubectl delete secret app -n floweryroad
kubectl delete secret auth -n floweryroad
```
## image 레지스트리에 푸시
```
docker push lunacircle4/app.floweryroad:1.0.0
```
## appling
```
export TAG=1.0.0
envsubst < app.yaml | kubectl apply -f -
```
## deployment 제거
```
envsubst < app.yaml | kubectl delete -f -
envsubst < auth.yaml | kubectl delete -f -
```
## pod 로깅 및 상태 확인
```
kubectl get pods -n floweryroad
kubectl describe deployment app -n floweryroad
kubectl describe pod app-77bfd5df59-lx6m4 -n floweryroad
kubectl logs app-77bfd5df59-lx6m4 -n floweryroad
```
## pod 내에 접속
```
kubectl exec -it app-77bfd5df59-lx6m4 bash -n floweryroad
```
## ingress 컨트롤러 설치 (nginx)
```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.48.1/deploy/static/provider/cloud/deploy.yaml
```
## ingress 컨트롤러 설치 (aws ingress)
```
kubectl apply --validate=false -f https://github.com/jetstack/cert-manager/releases/download/v1.0.2/cert-manager.yaml

curl -o iam-policy.yaml https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.2.0/docs/install/v2_2_0_full.yaml

kubectl apply -f ingress_base.yaml
```
## k8s kubeconfig 설정
```
aws eks --region ap-northeast-2 update-kubeconfig --name floweryroad
```
## ingress 적용
```
kubectl apply -f ingress.yaml -n floweryroad
```

## dump를 pod에 복사한후 psql이용하여 dumping 진행
```
kubectl cp ../../dumps app-77bfd5df59-x5q8r:/ -n floweryroad
```
## default database인 postgres에 먼저 접속하여 데이터베이스 생성
```
psql -d postgres -h host -U floweryroad
```
## dumping
```
psql -d floweryroad-auth -h host -U floweryroad < dump
psql -d floweryroad-app -h host -U floweryroad < dump
```
