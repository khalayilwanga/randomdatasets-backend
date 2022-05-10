# RandomDatasets backend

This is the flask backend to the RandomDatasets project found [here](https://github.com/khalayilwanga/randomdatasets-main).

It utilizes alembic to handle msql database migrations.  

## Dockerfile

In order to build the image for the backend you can use:  
`docker build -t image-name:image-version . `

or to pull the already built image you can use:  
`docker pull truphenak/randomdatasets-flask-backend:1.0.0`
