# Django Modeling
Django Rest Framework Modeling Task
version 1.0
## 0. Prerequisites
Python 3.8, Django 3.1, docker-compose 

docker push in [here repository packages](https://github.com/rimi-dev/modeling/packages)
## 1. Getting Started
- Git clone this project
### Run with docker-compose
installed docker
```shell script
docker-compose up
```
### Run
Change DATABASES(rds remark) in settings
```shell script
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Run TDD
Change DATABASES(rds remark) in settings
```shell script
py.test
```
### Resource Information
- 이사업체 정보/추가
    - EndPoint : /company/
- 고객 정보/추가
    - EndPoint : /customer/
- 가정이사 신청접수 정보/추가
    - EndPoint : /request/house/
- 차량 정보/추가
    - EndPoint : /car/
- 업체당 차량 소유 댓수 정보/추가
    - EndPoint : /car_count/
- 피드백 정보/추가
    - EndPoint : /feedback/

## 2. API Document
This Django Project's all API Information

[API Document](https://documenter.getpostman.com/view/10715220/TVCZZB54)

## 3. ERD Diagram
![image](https://user-images.githubusercontent.com/45389547/91257781-b6294700-e7a5-11ea-9c17-def3514b0a11.png)
[ERD Diagram Link](https://dbdiagram.io/d/5f45ec977b2e2f40e9dec60f)
***
Developer [@Rimi](https://github.com/rimi-dev)