# My FastAPI Sentiment analysis app

## Configuration

Create a file named `.env` in the root directory of the project. This file will contain the environment variables used by the application. 

You can use the `.env.example` file as a template.

## With docker

### Building the Docker image

To build the Docker image, run the following command:

```console
docker build -t my-app .
```

## Running the Docker container

To run the Docker container, use the following command:

```console
docker run --env-file .env -p 80:80 my-app
```


This command will start the container and map port 80 on the host machine to port 80 in the container. 

http://localhost/sentiment-analysis?movieID={movieID} will now return a JSON response with the sentiment analysis of the movie with the given ID.

http://localhost/sentiment-analysis?movieID=550 wil return the sentiment analysis of the movie with the ID 550 (Fight Club).


## Debugging

To debug the application, you can use the following command:

```console
uvicorn app.app:app --host 0.0.0.0 --port 80
```
