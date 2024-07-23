# Use Python 3.12 as the base image
FROM python:3.12

# Define build-time arguments to pass credentials and configuration
ARG EMAIL_SENDER=${EMAIL_SENDER:-""}
ARG EMAIL_PASSWORD=${EMAIL_PASSWORD:-""}
ARG EMAIL_RECEIVER=${EMAIL_RECEIVER:-""}
ARG HTML_PATH=${HTML_PATH:-""}

# Set environment variables for the application
ENV EMAIL_SENDER=${EMAIL_SENDER}
ENV EMAIL_PASSWORD=${EMAIL_PASSWORD}
ENV EMAIL_RECEIVER=${EMAIL_RECEIVER}
ENV HTML_PATH=${HTML_PATH}

# Create a directory for the application
RUN mkdir /app
# Copy the Python application files into the container
COPY ./src /app/src
COPY ./pyproject.toml /app

WORKDIR /app

# Set PYTHONPATH to include the current working directory
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

# Install Poetry for managing dependencies
RUN pip3 install poetry
# Configure Poetry to not create a virtual environment and install dependencies
RUN poetry config virtualenvs.create false && poetry install

# Set the entrypoint command to run the application with Poetry
ENTRYPOINT [ "poetry", "run", "mailingbot" ]
