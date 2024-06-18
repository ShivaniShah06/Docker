# Optimized docker image file. However in this case, optimizing does not help much as we cannot use distroless image
# because it does not allow us to run `fastapi` command

# Using lighter version of python base image
ARG PYTHON=python:3.12-slim
FROM $PYTHON AS build
# Set work directory so all subsequent commands run from this directory
WORKDIR /webapp
# Copy requirements.txt to /webapp
COPY requirements.txt ./
# Create a virtual environment that can be copied into the next stage and install requirements in it
RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Second stage using the same base image
FROM $PYTHON
# Setting work directory for 2nd stage
WORKDIR /webapp
# Copy the virtual environment from the first stage
COPY --from=build /venv/ /venv/
# Set PATH with the location where requirements are installed so that container can run `fastapi` command
ENV PATH=/venv/bin:$PATH
# Copy all the files in the current directory on the host to /webapp on the container
COPY . .
# Create user so that app does not run as a root user
RUN useradd webapp
USER webapp
# Commands to run the app. CMD can be overwritten by appening values to the command. Entrypoint ideally remains intact
CMD [ "--host", "0.0.0.0"]
ENTRYPOINT ["fastapi", "dev", "webapp.py"]




# Working code:
# FROM python:3.12-slim AS build-env
# WORKDIR /webapp
# # Copy every file in current directory to the /webapp directory on the container
# COPY . .
# # Install dependencies for the application using pip
# RUN pip3 install -r requirements.txt

# RUN useradd webapp
# USER webapp

# CMD ["fastapi", "dev", "webapp.py", "--host", "0.0.0.0"]