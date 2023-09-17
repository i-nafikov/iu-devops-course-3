# Innopolis University DevOps [F23] | Kotlin 

## Overview
The service provides information about current time in Europe/Moscow timezone.

## Build
### Building application on host machine
To run the application go to the `./app_kotlin` directory and run the following command:
```shell
./gradlew boot
```
### Building application Docker image
To build the application Docker image go to the `./app_kotlin` directory and run the following command:
```shell
docker build --tag iskanred/app_kotlin:1.0.0 .
```

## How to test?
In the latest version of the project there are 2 tests.
To run tests go to the `./app_kotlin` directory and run the following command:
```shell
./gradlew test
```

## How to run?
### GitHub repository.
1. Clone this repo.
2. Go to the `./app_kotlin` directory of the cloned repo.
3. Run the following command:
    ```shell
    ./gradlew bootRun
    ```
4. Now the service can be used
### Docker
1. Pull the image from Docker Hub (you can skip this step if you already have the image):
    ```shell
    docker pull iskanred/app_kotlin:1.0.0
    ```
2. Run a container based on this image:
    ```shell
    docker run -p 8080:8080 --name app_kotlin iskanred/app_kotlin:1.0.0
    ```
3. Now the service can be used

## Usage
The server's URL is `http://127.0.0.1:8080/`.
Obtain the page from the browser or make a GET request from any HTTP client.
The resulting response is a text string with current Moscow time.

## Contact
* Author: Iskander Nafikov
* E-mail: i.nafikov@innopolis.university