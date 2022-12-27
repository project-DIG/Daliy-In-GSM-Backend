FROM python:3.10.5

ENV PYTHONUNBUFFERED 1

ENV PATH="/scripts:${PATH}"

ENV ENV=dev

WORKDIR /app

COPY . .

COPY ./scripts /scripts

RUN pip install -r requirements.txt --no-cache-dir 

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser user --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user

CMD ["entrypoint.sh"]