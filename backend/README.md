# Backend
MAKI api를 위한 django 앱 폴더
개발용 db는 sqlite

## Backend 초기 설정

1. 패키지 설치
```shell
pip install -r requirements.txt
```

2. django 최초 DB 마이그레이션
```shell
python manage.py migrate
```

3. 최초계정 admin 계정 만들기
```shell
python manage.py createsuperuser
> Username: admin
> Email address: [Enter]
> Password: 1234
> Password (again): 1234
> Bypass password validation and create user anyway? [y/N]: y
```

## Backed 실행
```shell
python manage.py runserver
```

## Backend 코드 수정 시
```shell
pip install -r requirements.txt
python manage.py migrate
```
