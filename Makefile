DB = weatherman

all:
	python3 main.py

db_create:
	@PGPASSWORD=password  psql -U trtp -d postgres -c "create database $(DB)"

db_drop:
	@PGPASSWORD=password  psql -U trtp -d postgres -c "drop database $(DB)"

db:
	psql -U client -d $(DB) -p 5432 


init: db_drop db_create all