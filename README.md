# FastAPI Project Notes

This is a FastAPI project with Docker support.

## Project Structure

- **app**: This directory contains the main application code.
- **alembic**: This directory contains database migration scripts.

## Requirements

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/mamatkul/notes-backend.git
    cd notes-backend
    ```

2. Build and start the Docker containers:

    ```bash
    sudo docker-compose up --build
    ```

3. The FastAPI app should be running at [http://localhost:8000](http://localhost:8000).

5. To stop the containers, press `Ctrl + C` in the terminal where they are running.

## Database

- PostgreSQL database is used in this project.
- Database connection details:
  - **Host:** localhost
  - **Port:** 5433
  - **Username:** postgres
  - **Password:** postgres
  - **Database:** postgres

## Environment Variables

- **ALEMBIC_DATABASE_URL:** PostgreSQL database URL for Alembic Migrations.
- **APP_PORT:** Port on which the FastAPI app runs.


- To access the Docker container shell:

    ```bash
    sudo docker exec -it notes-backend sh
    ```

