FROM python:3.8
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt
RUN mkdir -p /proc
RUN /bin/bash -c "/usr/bin/mysqld_safe --skip-grant-tables &" && \
  sleep 5 && \
  mysql -u root -e "CREATE DATABASE mydb" && \
  mysql -u root mydb < /tmp/dump.sql