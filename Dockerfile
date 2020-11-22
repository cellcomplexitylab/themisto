FROM ubuntu:20.04

# RStudio Server version
ARG RSTUDIO=1.3.959

# Disable Prompt During Packages Installation
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    gdebi-core \
    python-dev \
    python3-pip \
    r-base=3* \
    wget

# Set Python 3 as default (over Python 2).
RUN update-alternatives --install \
    /usr/bin/python python /usr/bin/python3 10

# Install Jupyter
RUN pip3 -q install --upgrade pip && pip3 install jupyter

# Install RStudio
RUN wget -q https://download2.rstudio.org/server/bionic/amd64/rstudio-server-${RSTUDIO}-amd64.deb \
    && gdebi --non-interactive rstudio-server-${RSTUDIO}-amd64.deb

# Clean up after installation
RUN apt-get clean && rm -rf /var/lib/apt/lists/* \
    && rm rstudio-server-${RSTUDIO}-amd64.deb
