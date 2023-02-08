sudo apt-get update<br>
sudo apt-get install virtualenv postgresql libpq-dev<br>
sudo nano /etc/postgresql/14/main/pg_hba.conf<br>
local all   postgres    trust<br>
local all   all         md5<br>
(save)<br>
sudo systemctl restart postgresql<br>
sudo su - postgres<br>
psql<br>
create database flaskdemodb<br>
create user flaskdemouser with encrypted password 'password'<br>
grant all privileges on database flaskdemodb to flaskdemouser<br>
\q<br>
exit<br>
mkdir -p flaskapp/project1<br>
cd flaskapp<br>
virtualenv --python=/usr/bin/python3<br> .
source bin/activate<br>
cd ..<br>
cd flaskapp/project1<br>

