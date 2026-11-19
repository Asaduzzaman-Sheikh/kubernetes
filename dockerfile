# Build the Docker image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
COPY app.py /app/
COPY templates /app/templates
COPY static /app/static 

# Run pip to install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]