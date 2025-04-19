FROM python:3.8-slim-buster

# Install system dependencies
RUN apt update && apt upgrade -y && apt install -y git

# Set work directory early
WORKDIR /fwdbot

# Copy only requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all files into the container
COPY . .

# Make sure the start script is executable
RUN chmod +x start.sh

# Start the bot
CMD ["bash", "start.sh"]
