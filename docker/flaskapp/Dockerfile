
# syntax=docker/dockerfile:1<br>
<br>
FROM python:3.8-slim-buster<br>
<br>
WORKDIR /python-docker<br>
<br>
COPY requirements.txt requirements.txt<br>
RUN pip3 install -r requirements.txt<br>
<br>
COPY . .<br>
<br>
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]<br>
