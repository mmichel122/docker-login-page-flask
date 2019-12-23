FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV db_ip=127.0.0.1
ENV db_user=login
ENV db_pass=123456

CMD python app.py ${db_ip} ${db_user} ${db_pass}
