# assignment
>modeling Task
## 0. Prerequisites
Python 3.8, Django 3.1, docker-compose 

docker push in [here repository packages](https://github.com/rimi-dev/modeling/packages)
## 1. Installation Process
Use the package manager [pip](https://pypi.org/project/pip/) to install foobar.
```bash
pip install -r requirements/development.txt
```
### Install issue
psycopg2 install issue in macOS.
```bash
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2
```
1. 출처: [Link](https://stackoverflow.com/a/39244687)
## 2. Getting Started
### Run
```bash
python manage.py runserver
```

### Resource Manifest
- 이사업체 정보
    - EndPoint : /company/
- 고객 정보
    - EndPoint : /customer/
- 가정이사 신청접수 정보
    - EndPoint : /request/house/
- 차량 정보 
    - EndPoint(Create, Read) : /car/
    - EndPoint(Update, Delete) : /car/<:pk>