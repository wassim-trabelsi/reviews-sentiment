# My FastAPI App

## Building the Docker image

To build the Docker image, run the following command:

```console
docker build -t my-app .
```

## Running the Docker container

To run the Docker container, use the following command:

```bash
docker run -p 80:80 my-app
```


This command will start the container and map port 80 on the host machine to port 80 in the container. 

http://localhost/sentiment-analysis?movieID={movieID} will now return a JSON response with the sentiment analysis of the movie with the given ID.


