FROM python:3.6

RUN cd / && mkdir /app
WORKDIR /app

RUN apt-get update && \
	apt-get install -y vim

COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["server.py"]
