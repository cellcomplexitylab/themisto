# **Using the RStudio/Jupyter Notebook container**

## Quickstart

Introduction: This image allows you to run RStudio and Jupyter Notebook in browser

Visit ```localhost:8787``` in your browser to get access to RStudio and ```localhost:8888``` for Jupyter notebook.

## Common configurations options

### Building an image

```bash
docker build -t your_image_name .
```

This is to build your image after cloning the Docker file to your directory.

### Running the container with a shared volume

```bash
docker run --name your_container_name --rm -d -v $(pwd):/home/cclab/share -p 8787:8787 -p 8888:8888 -e DISABLE_AUTH=true your_image_name
```

```--rm``` means automatically remove the container when it exits

```-p``` means publishing a container’s port(s) to the host
