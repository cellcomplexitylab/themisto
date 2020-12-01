FROM rocker/rstudio:3.6.3

RUN apt-get update && apt-get install -y \
    python3 \
    python3-dev \
    python3-pip \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Jupyter
RUN pip3 -q install --upgrade pip && pip -q install jupyter

# Set Python 3 as default (over Python 2).
RUN update-alternatives --install \
    /usr/bin/python python /usr/bin/python3 10

RUN useradd cclab \
   && echo "cclab:cclab" | chpasswd \
   && mkdir /home/cclab \
   && mkdir /home/cclab/rstudio \
   && mkdir /home/cclab/notebook \
   && mkdir /home/cclab/share \
   && chown cclab:cclab /home/cclab \
   && addgroup cclab staff

ENV HOME=/home/cclab
ENV USER=cclab

# Jupyter setup
RUN mkdir -p /etc/services.d/notebook \
    && echo "#!/usr/bin/with-contenv bash \
        \nmkdir -p ${HOME}/notebook && chown ${USER}:${USER} ${HOME}/notebook \
        \nexec s6-setuidgid ${USER} /usr/local/bin/jupyter-notebook --no-browser --port=8888 --ip=0.0.0.0 --NotebookApp.token='' --notebook-dir=${HOME}/notebook" \
        > /etc/services.d/notebook/run

# Network port for Jupyter
EXPOSE 8888

CMD ["/init"]
