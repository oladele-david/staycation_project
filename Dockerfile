# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app-server

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Define the environment variable for Flask
ENV FLASK_APP run.py

# Run the application using Flask's built-in server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]