FROM python:3.9-buster

WORKDIR /backend

ADD requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/backend/entrypoint.sh" ]
