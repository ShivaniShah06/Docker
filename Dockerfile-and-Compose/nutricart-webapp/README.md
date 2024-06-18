# DOCKERFILE AND DOCKER COMPOSE

### PREREQUISITES
- Docker installed on your host

## BUILD AND PUSH THE DOCKER FILE FOR `nutricart-webapp`

> [!NOTE]
> The application will not run without postgresql database so make sure to follow the entire `README` file

- There are two dockerfiles in this directory:

   1. Dockerfile:
      - Optimized file with less image size i.e. 259MB
      - Used multi-stage technique

   2. Dockerfile-v1 
      - Non-optimized file with a little bigger size i.e. 277MB

    Ideally multi-stage images are lesser in size but for our particular use case, using this technique does not make much of a difference to not using it.

- Login to docker hub using your credentials (create account from docker hub web-interface before this step):
  
  ```shell
  docker login
  ```
- Run below command to build the docker image:
  
  ```shell
  docker build --no-cache --progress plain -t <your-docker-username>/<app_name>:<tag> -f Dockerfile .
  ```

  NOTE: An image of this app has already been created and available to use - `shivanishah612/webapp:no-env-v1`

- Push the file to docker hub:
  ```
  docker image push <image_name>

  eg: docker image push shivanishah612/webapp:no-env-v1
  ```

## RUN MANUALLY WITH POSTGRESQL

- The application requires Postgresql database in order to function

- Create a network to be shared between the postgres container and the application container for communication:

  ```shell
  docker network create <network_name>

  eg: docker network create test

  ```

- Spin up a Postgresql container:
  
  ```shell
  docker run --name <database_container_name> -e POSTGRES_USER=<postgres_user> -e POSTGRES_PASSWORD=<postgres_password> -e POSTGRES_DB=<postgres_db> -p <host_port>:<container_port> --network <network_name> <postgres_image>

  eg: docker run --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -p 5432:5432 --network test postgres:15.7
  ```

- Spin up the application container:
 
  ```shell
  docker run --name <application_container_name> -e DATABASE_URL=<postgres_database_url> -p <host_port>:<container_port> --network <network_name> <application_image_name>

  eg: docker run --name webapp -e DATABASE_URL=postgresql://postgres:postgres@postgres/postgres  -p 8000:8000 --network test shivanishah612/webapp:no-env-v1
  ```

## RUN ENTIRE APPLICATION WITH DOCKER COMPOSE

- A docker compose file (compose.yml) has already been written which can be used here to run this application as a package with a single command without having to run multiple commands and worrying about network configuration
- You will need 3 files as per your requirement in the same folder as the compose.yml:

   1. `postgres_user.txt`:
       - This is used as a secret in the compose file
       - You do not commit it in the version control system ideally as it is a sensitive information (I will commit it for the reference with some dummy value)
    2. `postgres_password.txt`:
        - This is used as a secret in the compose file
       - You do not commit it in the version control system ideally as it is a sensitive information (I will commit it for the reference with some dummy value)
    3. `.env`:
        - An environment variable refers to this file to look for a value i.e. DATABASE_URL
        - You do not commit it in the version control system ideally as it is a sensitive information (I will commit it for the reference with some dummy value)

- Run below command to make the entire application run:
  
  ```shell
  docker compose up
  ```

- Run below command to delete the application containers:

   ```shell
   docker compose down
   ```