# It is a file with instruction and argument.
# It can have any base package
# Use base package
FROM ubuntu:latest 

# Set working directory for the container
WORKDIR /app

# Copy all files in the current folder to the working directory on the container 
COPY . /app

# Update packages and install python3 and pip
RUN apt-get update && apt-get install -y  python3 python3-pip

# Run application using following command
CMD ["python3", "app.py"]


# Run following commands after writing this file:
#    1. `docker build -t <dockerhub_username/<image_name>> .` command
#    2. `docker login` --> Use docker hub credentials
#    3. `docker push <dockerhub_username/<image_name>>:latest`