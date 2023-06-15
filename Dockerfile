FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10
COPY . /app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "15400" ]