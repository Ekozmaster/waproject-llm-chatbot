FROM python:3.12.8-alpine3.21

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
VOLUME ["/app/.data"]
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
