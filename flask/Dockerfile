#https://hub.docker.com/_/python
# Use an official Python runtime as a parent image
FROM python:3.8-slim
RUN apt-get update && apt-get install -y procps less
RUN pip install flask
RUN pip install redis
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container as /app
COPY flask_app_k8_demo_p1.py /app

# Make port 80 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD python flask_app_k8_demo_p1.py
