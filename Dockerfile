FROM ubuntu:20.04

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    python3 \
    python3-dev \
    python3-pip \
    r-base=3* \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 -q install --upgrade pip && pip3 install jupyter
