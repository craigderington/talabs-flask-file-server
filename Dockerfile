FROM python:3.6-alpine
LABEL maintainer="Craig Derington <cderington@championsg.com>"
RUN apk update && apk upgrade
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "app.py"]
