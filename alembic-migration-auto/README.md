# alembic auto generating migrations

Build object model first then auto generate alembic migrations.

https://alembic.sqlalchemy.org/en/latest/autogenerate.html

```
docker compose up -d
```

Init:
```
alembic init myapp
```

Tasks:
- Configure `alembic.ini` for `sqlalchemy.url` connection string
- Configure `target_metadata` as per tutorial^^ to point to model module
- Work on `mymodel` module for data model

Generate migrations:
```
alembic revision --autogenerate -m "add initial models"
```

Migrate:
```
alembic history --verbose
alembic upgrade head
```

```
docker compose exec -it postgres psql -U alembic -d alembic -c "select * from public.alembic_version"
 version_num
--------------
 0537c8292aa9
(1 row)

docker compose exec -it postgres psql -U alembic -d alembic -c "\dt"
             List of relations
 Schema |      Name       | Type  |  Owner
--------+-----------------+-------+---------
 public | address         | table | alembic
 public | alembic_version | table | alembic
 public | user_account    | table | alembic
(3 rows)

docker compose exec -it postgres psql -U alembic -d alembic -c "\dS public.user_account"
                                    Table "public.user_account"
  Column  |         Type          | Collation | Nullable |                 Default
----------+-----------------------+-----------+----------+------------------------------------------
 id       | integer               |           | not null | nextval('user_account_id_seq'::regclass)
 name     | character varying(30) |           | not null |
 fullname | character varying     |           |          |
Indexes:
    "user_account_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "address" CONSTRAINT "address_user_id_fkey" FOREIGN KEY (user_id) REFERENCES user_account(id)

docker compose exec -it postgres psql -U alembic -d alembic -c "\dS public.address"
                                     Table "public.address"
    Column     |       Type        | Collation | Nullable |               Default
---------------+-------------------+-----------+----------+-------------------------------------
 id            | integer           |           | not null | nextval('address_id_seq'::regclass)
 email_address | character varying |           | not null |
 user_id       | integer           |           | not null |
Indexes:
    "address_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "address_user_id_fkey" FOREIGN KEY (user_id) REFERENCES user_account(id)
```

Tear down:
```
docker compose down
```
