FROM registry.access.redhat.com/ubi8/python-38
USER 0
RUN mkdir /app
WORKDIR /app
COPY ./main.py /app/
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
