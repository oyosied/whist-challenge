FROM python:3.8-slim
WORKDIR /app1
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python", "-u", "app.py"]