FROM registry.access.redhat.com/ubi8/python-38
USER 0
RUN mkdir /app
WORKDIR /app
COPY ./app.py /app/
COPY ./requirements.txt /app/
COPY ../cpu_pack/* /app/
RUN dnf install -y numactl util-linux
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
