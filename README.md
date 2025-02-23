# ETL API Python for FOLIO

## Overview
This project provides a simple ETL (Extract, Transform, Load) process exposed through a REST API built with Flask. The API includes an endpoint to trigger the ETL process and returns the results.

The project includes Swagger documentation using **Flask-RESTx**.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3
- pip (Python package manager)

## Installation
### 1. Clone the Repository
```sh
git clone <repository_url>
cd <repository_folder>
```

### 2. Create a Virtual Environment
```sh
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Unit Tests 

```sh
pip install pytest flask-testing
pytest


```

## Running the Application
To start the Flask application, run:
```sh
python3 main.py
```

The API will be available at:
```
http://localhost:5001/
```

## API Documentation (Swagger)
The API documentation is available at:
```
http://localhost:5001/swagger-ui/
```
You can also access the raw Swagger JSON at:
```
http://localhost:5001/swagger.json
```

## API Endpoints
### Run ETL Process
**Endpoint:**
```
POST /etl/run-etl
```

**Description:**
Triggers the ETL process and returns the status of each processed user.

**Response Example:**
```json
{
  "message": "ETL process completed",
  "data": [
    {
      "user_id": 123,
      "status": "processed"
    }
  ]
}
```

## Dependencies
This project uses the following dependencies:
- Flask
- Flask-RESTx
- Pandas
- Requests
- OpenPyXL
- SendGrid (for email notifications, if applicable)

To install dependencies separately:
```sh
pip install flask pandas requests openpyxl flask-restx sendgrid
```

## Deployment
To deploy this API on a production server, consider using **Gunicorn**:
```sh
pip install gunicorn
```
Run the application with:
```sh
gunicorn -w 4 -b 0.0.0.0:5001 main:app
```

## Swagger Documentation

![alt text](<Captura de Tela 2025-02-23 às 12.52.59.png>)

## Additional Resources
- Instance Data API Example:
  [`https://folio-quesnelia-okapi.dev.folio.org/inventory/instances`](https://folio-quesnelia-okapi.dev.folio.org/inventory/instances)

## License
This project is licensed under the MIT License.

