kubectl cp 

psql -h floweryroad-app.c4jyugmueru1.ap-northeast-2.rds.amazonaws.com -p 5432 -U ekstest -d floweryroad-app

psql -h floweryroad-auth.c4jyugmueru1.ap-northeast-2.rds.amazonaws.com -p 5432 -U ekstest -d floweryroad-auth
