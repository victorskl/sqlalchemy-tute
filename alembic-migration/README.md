# alembic migration

https://alembic.sqlalchemy.org/en/latest/tutorial.html

## Primer

```
docker compose up -d
docker compose exec -it postgres psql -U alembic -d alembic
alembic=# \l
alembic=# \?
alembic=# \q
```

```
which alembic
alembic --help
alembic list_templates
```

```
alembic init myapp
vi alembic.ini
```

## First Migration

```
alembic revision -m "create account table"
vi myapp/versions/eeb207c3a636_create_account_table.py
alembic upgrade head
```

```
docker compose exec -it postgres psql -U alembic -d alembic -c "\dt"
             List of relations
 Schema |      Name       | Type  |  Owner
--------+-----------------+-------+---------
 public | account         | table | alembic
 public | alembic_version | table | alembic
(2 rows)
```

```
docker compose exec -it postgres psql -U alembic -d alembic -c "\dS public.account"
                                      Table "public.account"
   Column    |          Type          | Collation | Nullable |               Default
-------------+------------------------+-----------+----------+-------------------------------------
 id          | integer                |           | not null | nextval('account_id_seq'::regclass)
 name        | character varying(50)  |           | not null |
 description | character varying(200) |           |          |
Indexes:
    "account_pkey" PRIMARY KEY, btree (id)
```

## Second Migration

```
alembic revision -m "add a column"
vi myapp/versions/e11b78f921ad_add_a_column.py
alembic upgrade head
```

```
docker compose exec -it postgres psql -U alembic -d alembic -c "\dS public.alembic_version"
                    Table "public.alembic_version"
   Column    |         Type          | Collation | Nullable | Default
-------------+-----------------------+-----------+----------+---------
 version_num | character varying(32) |           | not null |
Indexes:
    "alembic_version_pkc" PRIMARY KEY, btree (version_num)
```

```
docker compose exec -it postgres psql -U alembic -d alembic -c "select * from public.alembic_version"
 version_num
--------------
 e11b78f921ad
(1 row)
```

## Migrations

(skip this section, just a note)

```
alembic current
```

```
alembic upgrade e11
alembic upgrade +2
alembic upgrade -1
alembic upgrade ae10+2
```

```
alembic history --verbose
alembic history -r1975ea:ae1027
alembic history -r-3:current
alembic history -r1975ea:
```

Reset:
```
alembic downgrade base
```

## Tear Down

```
docker compose down
```
