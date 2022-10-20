FROM python:3.8

WORKDIR /app
ADD ./requirements.txt .
RUN echo "b" | pip install -r requirements.txt
ADD . .
RUN echo "y" | python /app/sarenka/sarenka.py

EXPOSE 8000

CMD ["python", "/app/sarenka/backend/manage.py", "runserver", "0.0.0.0:8000"]