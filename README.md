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
- Tools for integration:
  - **Nmap**
  - **Wireshark**
  - A DHCP Manager compatible with your network setup.

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
