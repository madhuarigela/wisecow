FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y \
    fortune-mod \
    fortunes \
    cowsay \
    netcat-openbsd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY wisecow.sh .

# Convert Windows CRLF to Linux LF
RUN sed -i 's/\r$//' wisecow.sh && chmod +x wisecow.sh

ENV PATH="/usr/games:${PATH}"

EXPOSE 4499

CMD ["bash", "wisecow.sh"]