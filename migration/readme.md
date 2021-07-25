# 기존 데이터베이스에서 새로운 데이터베이스로의 마이그레이션

## 마이그레이션한 과정
1. 먼저 새로운 데이터베이스를 구축 한다.

2. django migrate에 의해 새롭게 구축된 테이블만 존재하는 데이터베이스의 dump와 기존 데이터베이스의 dump를 뜬다.
```
psql xxx -U xxx < dump
```

3. 기존 데이터베이스에 데이터를 뽑아 새 데이터베이스에 이식하는 python script를 작성한후 필요한 테스트 환경에 필요한 환경변수 파일들(old.env, new.env, connection.env)을 준비하여 도커 환경에서 테스트 한다.
```
docker-compose up

# 각각의 도커 테스트 환경에 새로운 데이터베이스, 기존 데이터베이스 덤프 적용
pg_dump xxx -U xxx > dump

# 테스트
python3 tests.py
python3 main.py
```

4. 실제 환경의 환경변수 파일(connection.env)을 준비하여 테스트된 스크립트로 새로운 데이터베이스로의 마이그레이션을 진행한다. 이때 참조 무결성을 지키기 위해 마이그레이션하는 테이블의 순서를 유념하여 data.py를 작성한후 진행해야 한다.
```
# data.py 작성후 진행
python3 main.py
```
