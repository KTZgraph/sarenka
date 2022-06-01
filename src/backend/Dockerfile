# Generate workable requirements.txt from Poetry dependencies 
FROM python:3.10.4
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["python", "./manage.py", "runserver"]
