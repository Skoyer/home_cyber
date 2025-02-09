# FastAPI Cyber Project: Building a CRUD API with MVC Structure

This repository is a cyber project designed to streamline asset discovery and tracking using tools like **Nmap**, **DHCP Manager**, and **Wireshark**. Initially, this project is a basic implementation of a **FastAPI CRUD API** with a **PostgreSQL database** and an **MVC structure**. Currently, it writes test customer data to the database to ensure the foundational setup works correctly.

The project is in its early stages, with future plans to expand into scanning and storing network data in a PostgreSQL database for deeper analysis and automation.

---

## Current Features
- A **FastAPI** backend implementing basic CRUD functionality.
- Uses **PostgreSQL** as the database to store customer records (test data for now).
- **MVC structure** for a clean and scalable codebase.

## Planned Features
1. **Integration with Cybersecurity Tools**:
   - **Nmap**: Scan network devices and store results in the database.
   - **DHCP Manager**: Log and manage IP leases dynamically.
   - **Wireshark**: Analyze captured network traffic and track assets.
2. **Asset Discovery & Tracking**:
   - Automate discovery of devices on the network.
   - Create a comprehensive asset database with metadata.
3. **Data Analytics**:
   - Develop visualizations and reports on the tracked assets.
   - Detect anomalies or potential cybersecurity issues.
4. **Advanced API Development**:
   - Enhance the API to allow querying, filtering, and exporting data.

---

## Getting Started

### Prerequisites
- **Python 3.10+**
- **PostgreSQL 12+**
- **ChatGPT API Key**
- **Future** - Tools for integration:
  - **Nmap**
  - **Wireshark**
  - A DHCP Manager compatible with your network setup.

### Setup Instructions

# Setting Up and Running the Cyber Project

### Prerequisites
1. Ensure you have **PostgreSQL** set up and working.
2. Verify that you can connect to PostgreSQL using a valid `userid` and `password`.

---

### Step 1: Configure Database Connection

- Edit the `db/database.py` file.
- Create an `.env` file in the `db` directory and include the required connection parameters:

```plaintext
DB_USER=your_userid
DB_PASSWORD=your_password
DB_HOST=192.168.xx.yy
DB_PORT=5432
DB_NAME=cyber_project
```
---

### Step 2: Configure Test Environment
- Create a `.env` file in the `test` directory with the following parameters:
```plaintext
OPENAI_API_KEY=your_api_key
FASTAPI_URL=http://127.0.0.1:8080/api/customers/
```
---

### Step 3: Running the Application
- Navigate to the app directory.
- Start the application using the following command:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```
---

### Step 4: Testing the Application
# Option 1: Use Swagger UI
- Visit http://127.0.0.1:8080/docs to access the Swagger UI.
- Use the Swagger interface to test API endpoints.
# Option 2: Use the test Folder
- Utilize the test folder to create customers using tools like ChatGPT.
# Additional Reference:
Check out the  [Medium Article](https://verticalserve.medium.com/building-a-python-fastapi-crud-api-with-mvc-structure-13ec7636d8f2) for guidance on building and testing the application.