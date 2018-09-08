Title: Create user and database in Postgres
Author: Marc
Date: 2011-06-27 13:00:00
Slug: create-user-and-database-in-postgres
Tags: 

While I love Postgres, I get some problems every time I want to do the simple operation of creating a database with an associated user if it's been a while since the last time I did it.

There are several posts on the Internet about Postgres authentication, but I couldn't find any explaining exactly what I wanted to know, so here is mine.

This has been tested on **Debian 6** and **PostgreSQL 8.4**.

1. Install the PostgreSQL server (obvious)
2. Create the user:
<code>
$ sudo -u postgres createuser -D -A -P <my-user>
</code>
3. Create the database
<code>
$ sudo -u postgres createdb -O <my-user> <my-database>
</code>
4. Edit /etc/postgresql/8.4/main/pg_hba.conf
<code>
# Put your actual configuration here
local   all         all         password
host    all         all         127.0.0.1/32          password
</code>
**NOTE:** Make sure that your settings are placed after the comment saying where your configurations go. If you place them at the end, the default ones will be used, and you'll see this error when logging in:
<code>
psql: FATAL:  Ident authentication failed for user "<my-user>"
</code>

Actually, you'll probably want to customize the settings you want to use. My settings allow logging in from localhost using unencrypted password, but may be you want to access from another host, only grant access to some users or some databases, or use another authentication methods, so I would recommend you reading the [pg_hda.conf reference](http://developer.postgresql.org/pgdocs/postgres/auth-pg-hba-conf.html).

Finally, you'll be able to access by:
<code>
$ psql -U <my-user> -W
</code>