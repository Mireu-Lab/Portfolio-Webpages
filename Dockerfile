FROM python:3

RUN pip3 install flask
RUN mkdir project
WORKDIR /project

COPY . .

CMD [ "python3", "App/main.py" ]
