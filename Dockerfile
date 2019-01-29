FROM tensorflow/tensorflow:latest-gpu-py3
MAINTAINER "George Sohos, https://github.com/gsohos"

# Install system dependencies
RUN set -ex && \
	apt-get update && apt-get install -y \
	ca-certificates \
	sudo \
	libprotobuf-dev \
	protobuf-compiler \
	wget \
	git \
	software-properties-common \
	libssl-dev \
	libzmq3-dev \
	python3-dev \
	python3-pip \
	&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade pip setuptools wheel
RUN pip install --upgrade numpy keras
WORKDIR /app
COPY . /app

# ENV PATH /app:$PATH

CMD ["python", "/app/main.py"]

