FROM python:3.8

LABEL email="ihoryk@ukr.net"

COPY flask_blueprint/ flask_blueprint/

WORKDIR /flask_blueprint

RUN pip install -r requirements.txt

CMD ["python", "wsgi.py"]