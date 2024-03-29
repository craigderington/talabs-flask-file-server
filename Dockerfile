FROM python:3.6-alpine
LABEL maintainer="Craig Derington <cderington@championsg.com>"
RUN apk update && apk upgrade
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "2", "--log-level=INFO", "wsgi:app"]
