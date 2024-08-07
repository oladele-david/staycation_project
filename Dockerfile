# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app-service

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

# Copy the rest of the application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Run the application with Gunicorn, specifying the correct module and app variable
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]