# Docker container for RStudio & Jupyter Notebook

## Quickstart

The docker image specified in the `Dockerfile` allows you to run RStudio and
Jupyter Notebook in a browser.

Once the container is running (see below), enter the URL ```localhost:8787```
in your browser to get access to RStudio and ```localhost:8888``` for Jupyter
notebook. 

### Clone the repository

Assuming you `git` is installed on your computer, you can clone the repository
with the command below.
```bash
git clone https://github.com/cellcomplexitylab/dockerfiles
```

### Building the image

Change directory to the git repository.
```bash
cd dockerfiles
```

Assuming that `docker` is installed
on your computer, you can build the image with the command below.
```bash
docker build -t themisto:1.0 .
```

The image is called `themisto` version `1.0` for internal purposes, but you
can replace it with any other name and any other version number.

## Common running options

### Standard run

Once the image is built, you can start the Rstudio and Jupyter services
in your browser from any directory with the command below.
```bash
docker run --rm -v $(pwd):/home/cclab/share -p 8787:8787 -p 8888:8888 -e DISABLE_AUTH=true themisto:1.0
```

The directory from where you started `themisto` on the host is mapped
to the directory `/home/cclab/share` on the virtual machine. All the
files in this directory will be accessible to RStudio and Jupyter, and
reciprocally, all the outputs of Rstudio and Jupyter saved in this
directory will remain when the virtual machine is stopped (the others
will be destroyed).

To shutdown the virtual machine, enter `Ctrl-C` in the terminal
window or close the terminal.

_Explanation of the options:_  
   `--rm`: remove the container upon exit  
   `-v $(pwd):/home/cclab/share`: map the current directory to
`/home/cclab/share` on the virtual machine  
   `-p 8787:8787`: expose port 8787 of the virtual machine to port
8787 of the host  
   `-e DISABLE_AUTH=true`: required to run RStudio.


### Running the container with a different shared volume
You can map any directry of the host to `/home/cclab/share`. Whereas
the converse is also true, it is recommended to use only
`/home/cclab/share` on the virtual machine for sharing.

If you want to share the directory `/home/user` on the host, you can
start the virtual machine with the command below.
```bash
docker run --rm -v /home/user:/home/cclab/share -p 8787:8787 -p 8888:8888 -e DISABLE_AUTH=true themisto:1.0
```

### Running the container in the background
You can run the virtual machine in the background so that it does
not exit when you close the terminal. In this case, it is better
to give a name to the container so that you can shut it down
more easily.

You can start the virtual machine in the background by running
the command below.

```bash
docker run --name themisto --rm -dv /home/user:/home/cclab/share -p 8787:8787 -p 8888:8888 -e DISABLE_AUTH=true themisto:1.0
```

You can shut down the virtual machine by running the command
below.
```bash
docker stop themisto
```

_Explanation of the options:_  
   `--name themisto`: call container themisto  
   `-d`: detach (run in the background).  
