# quickstart app

https://docs.sqlalchemy.org/en/20/orm/quickstart.html

```
python main.py
```

Open and observe `quickstart.db` using [sqlite3 cli](https://sqlite.org/cli.html) like so:

```
sqlite3 quickstart.db

sqlite> .schema
CREATE TABLE user_account (
	id INTEGER NOT NULL,
	name VARCHAR(30) NOT NULL,
	fullname VARCHAR,
	PRIMARY KEY (id)
);
CREATE TABLE address (
	id INTEGER NOT NULL,
	email_address VARCHAR NOT NULL,
	user_id INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES user_account (id)
);

sqlite> select * from user_account;
1|spongebob|Spongebob Squarepants
2|sandy|Sandy Cheeks

sqlite> select * from address;
1|spongebob@sqlalchemy.org|1
3|sandy@squirrelpower.org|2

sqlite> select * from user_account join address on address.user_id = user_account.id;
1|spongebob|Spongebob Squarepants|1|spongebob@sqlalchemy.org|1
2|sandy|Sandy Cheeks|3|sandy@squirrelpower.org|2

sqlite> .quit
```
