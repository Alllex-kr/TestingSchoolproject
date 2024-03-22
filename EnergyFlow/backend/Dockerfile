FROM python:3.11

WORKDIR /fastapi/app

COPY requirements.txt /fastapi/app/requirements.txt
COPY . /fastapi/app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pymongo

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]