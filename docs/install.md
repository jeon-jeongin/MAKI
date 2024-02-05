# Install

## Dockerfile 개발 환경 실행

개발 환경을 위한 도커 파일을 실행 코드

```shell
# 도커파일을 이미지로 빌드합니다.
docker build -t maki_dev .

# 빌드한 이미지를 실행합니다.
docker run -v ${pwd}:/app/ --name maki_dev -dit --rm maki_dev
```
- VSCode Extension 에서 Remote Development 설치
- `Ctrl`or`Cmd` + `P`
- `> Dev Containers: Attach to Running Container...` 선택 
- `maki_dev` 선택


## Backend 실행

- api를 위한 django 앱 폴더
- 사용된 db는 sqlite

```shell
# backend 프로젝트 폴더로 이동
cd backend

# 패키지 설치
pip install -r requirements.txt

# django 구동을 위한 최초 DB 설정
python manage.py migrate

# 최초계정 supseruser을 만들기
python manage.py createsuperuser
> Username: admin
> Email address: [Enter]
> Password: 1234
> Password (again): 1234
> Bypass password validation and create user anyway? [y/N]: y

# db에 샘플데이터를 생성
python -m data.create_data
```



## Frontend 실행

- 새로운 터미널 오픈
- 화면 개발을 위한 프론트서버를 실행

```shell
# frontend 프로젝트 서버로 이동합니다.
cd frontend

# 패키지를 설치합니다.
yarn

# 서버를 실행합니다.
yarn dev
```