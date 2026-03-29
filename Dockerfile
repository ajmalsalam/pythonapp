FROM python:3.11-slim
WORKDIR /pythonapp
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 7000
CMD ["python","app.py"]
