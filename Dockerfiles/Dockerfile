# Use a base image with kubectl
FROM bitnami/kubectl:latest AS kubectl

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Copy kubectl from the first stage
COPY --from=kubectl /opt/bitnami/kubectl/bin/kubectl /usr/local/bin/kubectl

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# # Define environment variable
# ENV NAME World

# Run the application
CMD ["python", "BasicTui.py"]