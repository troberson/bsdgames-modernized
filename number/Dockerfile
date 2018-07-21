FROM python:3.7-alpine

WORKDIR bsdnumber/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
