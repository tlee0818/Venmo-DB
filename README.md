# Venmo-DB
Emulation of what Venmo Database might look and function like

pspgSql Database
Creators: Takho Lee, Even Feder, Eileen Mao

## Get Started

1. Running initialize.sql will call the create file, populate the database, and create some essential triggers.

2. In terminal, run: 

	```
	psql -d Postgres -U user -f initialize.sql
	```

3. User stories are reflected in the .py files. Run with:
	```
	python query_name.py
	```
4. Running show_all before and after calling a .py file will reflect appropriate changes in the Database. Run: 
	```
	psql -d Postgres -U user -f show_all.sql
	```
