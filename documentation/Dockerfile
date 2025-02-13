# Base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r /app/requirements.txt

# Copy the mkdocs.yml file
COPY mkdocs.yml /app/

# Copy the docs directory to the container
COPY docs /app/docs

# Expose port 8000
EXPOSE 8000

# Command to run the mkdocs server
CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]
