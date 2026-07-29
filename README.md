# Employee Compensation Service

A REST API built using **Azure Functions (Python)** and **SQLite** for managing employee compensation data. The service provides CRUD operations for employees and report endpoints for compensation analytics.

## Features

- Employee CRUD operations
- SQLite database
- Azure Functions HTTP API
- Compensation reporting endpoints
- Configurable database path using environment variables

## Prerequisites

- Python 3
- Azure Functions Core Tools v4
- SQLite3

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd employee-compensation-service
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure local settings

Create a local configuration file by copying the example:

```bash
cp local.settings.example.json local.settings.json
```

### 5. Create the database

Run the provided SQL scripts to create and populate the SQLite database.

### 6. Start the Azure Function

```bash
func start
```

The API will be available at:

```
http://localhost:7071/api
```

## API Endpoints

### Employee

| Method | Endpoint |
|---------|----------|
| POST | `/api/employees` |
| GET | `/api/employees` |
| GET | `/api/employees/{id}` |
| PUT | `/api/employees/{id}` |
| DELETE | `/api/employees/{id}` |

### Reports

| Method | Endpoint |
|---------|----------|
| GET | `/api/reports/total-bonus` |
| GET | `/api/reports/no-bonus` |
| GET | `/api/reports/bonus-percentage` |
| GET | `/api/reports/high-bonus-departments` |
| GET | `/api/reports/bonus-ranking` |
| GET | `/api/reports/highest-compensation` |

## Notes

- SQLite foreign key constraints are enabled.
- The database path is configurable through the `DATABASE_PATH` environment variable.
- Employees without a stored bonus receive a default bonus of **5% of salary** when data is read. This value is calculated dynamically and is not written back to the database.