FROM python:3.8.2-slim

WORKDIR /code

COPY main.py requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]