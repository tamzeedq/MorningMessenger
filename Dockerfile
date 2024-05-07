# Dockerfile for the Python 3.11 image
FROM python:3.11.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install -r requirements.txt

# Run the application
CMD [ "python", "messenger.py" ]
