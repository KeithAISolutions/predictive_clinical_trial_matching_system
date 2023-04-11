FROM python:3.11-slim-buster

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential libssl-dev libffi-dev python3-dev git curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Docker
RUN curl -fsSL https://get.docker.com -o get-docker.sh && \
    sh get-docker.sh && \
    rm get-docker.sh

# Install Docker Compose
RUN curl -L "https://github.com/docker/compose/releases/download/v2.1.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

# Install Python packages
RUN python -m pip install --upgrade pip && \
    pip install pylint psycopg2-binary
