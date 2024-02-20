FROM registry.access.redhat.com/ubi8/python-38
USER 0
RUN mkdir /app
WORKDIR /app
COPY ./app.py /app/
COPY ./requirements.txt /app/
COPY ./cpu_pack/ /opt/app-root/src/
COPY ./cpu_pack/ /app/
RUN chmod -R 777 /app
RUN pip install -r requirements.txt
#CMD ["python3", "app.py"]
ENV LD_LIBRARY_PATH /app
CMD ["./numactl", "-C", "5", "python3", "app.py"]
