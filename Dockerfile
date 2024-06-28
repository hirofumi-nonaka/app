FROM python:3.9
WORKDIR /app
ADD . /app
RUN pip install Flask
RUN pip install pysqlite3
EXPOSE 8000
CMD ["python", "app.py"]
