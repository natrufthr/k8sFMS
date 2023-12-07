# Use a base image with kubectl
FROM bitnami/kubectl:latest AS kubectl

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Copy kubectl from the first stage
COPY --from=kubectl /opt/bitnami/kubectl/bin/kubectl /usr/local/bin/kubectl

# Copy your entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh

# Set the entrypoint script
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]