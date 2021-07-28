# eks 도입

## 준비 과정
1. 배포에 필요한 이미지 빌드

2. 로컬 환경에서 k8s배포해보고 프론트에서 테스트
    로컬 DB 가동
    secret 생성
    auth 생성
    app 생성
    ingress 생성
    로컬 프론트에서 테스트
    MSA의 경우 django 모델 object에서 user를 바로 사용하지 않고 user_id 사용에 주의

3. eks 괸련 자료 수집

4. eks 배포 및 프론트에서 테스트
