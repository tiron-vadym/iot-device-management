# IoT Device Management

This project is designed for managing IoT devices. It uses `PostgreSQL` for data storage, `Peewee` for ORM, `Aiohttp` for requests, and Docker for containerizing the services.

## Project Structure

- **db**: PostgreSQL database service
- **app**: Main Python application using FastAPI structure
- **test**: Service for running tests with pytest

## Getting Started

### Requirements

- Docker
- Docker Compose

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/tiron-vadym/iot-device-management
    cd iot-device-management
    ```

2. Create a `.env` file in the root directory of the project and add the following variables:
    ```dotenv
    POSTGRES_DB=your_database_name
    POSTGRES_USER=your_database_user
    POSTGRES_PASSWORD=your_database_password
    POSTGRES_HOST=db
    ```

### Running the Project

1. Start the services using Docker Compose:
    ```bash
    docker-compose up
    ```

2. The application will be accessible at `http://localhost:8000`.

### Database Migrations

Migrations are automatically run during the startup of the `app` container using `Peewee`.

## Endpoints

- Create device POST: `/devices/`
- Read devices GET: `/devices/`
- Read device GET: `/devices/{id}/`
- Update device PUT: `/devices/{id}/`
- Delete device DELETE: `/devices/{id}/`

### Running Tests

To run the tests, execute:
```bash
docker-compose run test
