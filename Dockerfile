FROM python:3.10.5


MAINTAINER Noh Gaseong <s21005@gsm.hs.kr>


RUN pip3 install django


WORKDIR /usr/src/app


COPY . .

WORKDIR ./letterproject
# manage.py를 실행할 수 있는 디렉토리로 이동합니다.

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# 이동한 디렉토리에서 django를 가동시켜주는 코드를 작성합니다. 여기서 port는 8000로 실행시키겠습니다.

EXPOSE 8000
# django 서버의 포트를 8000로 지정하였으므로 Docker의 컨테이너 또한 8000 포트를 열어줍니다.