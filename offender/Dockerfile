FROM registry.access.redhat.com/ubi8/python-38
USER 0
RUN mkdir /app
WORKDIR /app
COPY ./app.py /app/
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt && dnf install -y numactl util-linux*
CMD ["lscpu"]
CMD ["numactl", "-m", "0,1,2", "-N", "0,1,2", "python", "app.py"]
