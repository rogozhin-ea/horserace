FROM ubuntu

COPY . /home/horserace
WORKDIR /home/horserace

RUN apt-get update && apt-get install -y python3 && apt install -y python3-psycopg2

ENTRYPOINT ["bash"]
