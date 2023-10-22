# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# If you don't have a requirements.txt, you can install packages directly using pip
RUN pip install -r requirements.txt

# Define the command to run your Python script
CMD [ "python", "ippusher.py" ]