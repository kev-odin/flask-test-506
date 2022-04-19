### START CLASS IMAGE ###
FROM PYTHON:3.10-slim-buster as class_docker
RUN pip install email_validator flask flask-wtf flask-login flask-sqlalchemy requests
COPY app.py app.py
CMD python app.py