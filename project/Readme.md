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
pip install flask<br>
pip install flask-sqlalchemy<br>
pip install flask-migrate<br>
pip install psycopg2<br>

Copy the project directory to your local directory or cloud instance<br>
Run the following command to create necessary tables<br>
flask db init<br>
flask db migrate<br>
flask db upgrade<br>

Run the following command to execute the applicaation<br>
export FLASK_APP=run.py
flask run --host 0.0.0.0

