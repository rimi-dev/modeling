# assignment
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
### Install issue
psycopg2 install issue in macOS.
```shell script
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2
```
1. 출처: [Link](https://stackoverflow.com/a/39244687)
## 2. Getting Started
### Run
```shell script
python manage.py runserver
```

### Test
```shell script
pytest
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