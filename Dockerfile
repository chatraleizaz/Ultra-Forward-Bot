FROM python:3.8-slim-buster

# Install system dependencies
RUN apt update && apt upgrade -y && apt install -y git

# Copy and install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

# Create working directory
WORKDIR /fwdbot

# Copy all bot files into the container
COPY . /fwdbot

# Ensure start.sh is executable
RUN chmod +x /fwdbot/start.sh

# Run the start script
CMD ["/bin/bash", "/fwdbot/start.sh"]
