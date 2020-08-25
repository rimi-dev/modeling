# Django Modeling
modeling Task
version 1.0
## 0. Prerequisites
Python 3.8, Django 3.1, docker-compose 

docker push in [here repository packages](https://github.com/rimi-dev/modeling/packages)
## 1. Installation Process
Install requirements
```shell script
pip install -r requirements.txt
```
>:bangbang: Install issue
>
>psycopg2 install issue in macOS.
>```shell script
>env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2
>```
>출처: [Link](https://stackoverflow.com/a/39244687)
## 2. Getting Started
### Run
```shell script
python manage.py runserver
```

### Run TDD
```shell script
py.test
```
### Resource Information
- 이사업체 정보
    - EndPoint : /company/
- 고객 정보
    - EndPoint : /customer/
- 가정이사 신청접수 정보
    - EndPoint : /request/house/
- 차량 정보 
    - EndPoint(Create, Read) : /car/
    - EndPoint(Update, Delete) : /car/<:pk>

### API Document
This Django Project's all API Information

[API Document](https://web.postman.co/collections/10715220-64b21381-6b7c-4cdb-8d0a-ae076c9eb90c?version=latest&workspace=c42daf6d-5c3c-4ba2-865f-8b1c8007a65f)