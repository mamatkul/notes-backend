# Use the official Python image as the base image
FROM python:3.10-alpine

# system update & package install
RUN apk update && \
    apk add --no-cache \
    build-base \
    postgresql-dev \
    postgresql-client \
    openssl-dev

# Set the working directory inside the container
WORKDIR /app

# Copy the local contents into the container at /app
COPY . /app



# Install Poetry in the container & Install project dependencies from the pyproject.toml file
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh


EXPOSE 8000
# Command to start your FastAPI app (adjust this if your app has a different startup command)
CMD ["uvicorn", "main:fastapi_app", "--host", "0.0.0.0", "--reload",  "--port", "8000"]
