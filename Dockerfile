FROM python:3

RUN mkdir project
WORKDIR /project

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "src/main.py" ]
