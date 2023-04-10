# Use the latest official Python image as the base
FROM python:3.11.2

# Install necessary packages
RUN pip install --no-cache-dir tensorflow keras pandas opencv-python Flask docker git numpy scipy torch matplotlib

# Install TypeScript
RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g typescript
