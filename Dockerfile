FROM quay.io/bitnami/python:3.10-prod

RUN pip3 install flask ; \
    mkdir /webroot

COPY main.py /webroot/main.py

WORKDIR /webroot
ENV FLASK_APP=main
EXPOSE 5000/tcp

ENTRYPOINT ["flask"]
CMD ["run"]
