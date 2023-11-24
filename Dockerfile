# Use an official Python runtime as a parent image
FROM python:3.9.5-slim-buster

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container at /usr/src/app
COPY . .

# Run script.py when the container launches
CMD ["python", "./script.py"]
