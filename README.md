# assignment
## Project Info
### 1. Setting
Use the package manager [pip](https://pypi.org/project/pip/) to install foobar.
```bash
pip install -r requirements/development.txt
```
#### Install issue
psycopg2 install issue in macOS.
```bash
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2
```
1. 영문 [Link](https://stackoverflow.com/a/39244687)
### 2. Run
1. local
```bash
python manage.py runserver
```