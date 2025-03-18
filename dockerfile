# Use the official Python image as a base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the poetry.lock and pyproject.toml to install dependencies first
COPY pyproject.toml poetry.lock /app/

# Install system dependencies and Poetry
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev && \
    pip install poetry

# Install Python dependencies using Poetry
RUN poetry install --no-dev

# Copy the entire project into the container
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Set the environment variable for Django settings
ENV DJANGO_SETTINGS_MODULE=twitterclone.settings

# Run Django migrations (optional step)
CMD ["poetry", "run", "python", "manage.py", "migrate"]
