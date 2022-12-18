FROM python:3.10

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /app

COPY * ./

CMD [ "python", "main.py" ]