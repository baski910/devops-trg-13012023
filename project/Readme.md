sudo apt-get update
sudo apt-get install virtualenv postgresql libpq-dev
sudo nano /etc/postgresql/14/main/pg_hba.conf
local all   postgres    trust
local all   all         md5
(save)
sudo systemctl restart postgresql
sudo su - postgres
psql
create database flaskdemodb
create user flaskdemouser with encrypted password 'password'
grant all privileges on database flaskdemodb to flaskdemouser
\q
exit
mkdir -p flaskapp/project1
cd flaskapp/project1
