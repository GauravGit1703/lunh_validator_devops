#use an official python base image
FROM python:3.11-slim

#set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

#set work directory inside the container

WORKDIR /app

#copy project files
COPY . /app 

#install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#expose port Flask runs on 
EXPOSE 5000

#run the flask app

CMD ["python","app.py"]


