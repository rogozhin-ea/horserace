FROM ubuntu

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY . /home/horserace
WORKDIR /home/horserace

RUN apt-get update && apt-get install -y python3 && apt install -y python3-psycopg2 

ENTRYPOINT ["bash"]
