FROM ubuntu

COPY . /home/horserace
WORKDIR /home/horserace

ENV VIRTUAL_ENV=/opt/venv
RUN apt-get update && apt-get install -y python3 && apt install -y python3-psycopg2 && apt install python3.10-venv && python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENTRYPOINT ["bash"]
