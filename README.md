# **Using the RStudio/Jupyter Notebook container**
## Quickstart 
Intro: This image is used to have RStudio and Jupyter Notebook running in browser
```
docker run --name yourbranchhere --rm -p 8787:8787 -p 8888:8888 -e DISABLE_AUTH=true yourfilename
```
Visit ```localhost:8787``` in your browser to get access to RStudio and ```localhost:8888``` for Jupyter notebook
