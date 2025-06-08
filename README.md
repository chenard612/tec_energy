# Tec Energy Exercice

A FastAPI application that downloads CSV files describing natural gas shipments, parses and validates them, and inserts the data into a PostgreSQL database.

---

## Technologies Used

- **FastAPI** (async Python web framework)
- **Uvicorn** (ASGI server)
- **SQLAlchemy** (ORM)
- **PostgreSQL** (relational database)
- **Docker Compose** (for running PostgreSQL locally)
- **BeautifulSoup** & **Requests** (for HTML parsing and HTTP requests)

---

## Requirements

- Python 3.10+
- Docker & Docker Compose

---

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/chenard612/tec_energy.git
cd tec_energy

python3 -m venv .tecvenv
source .venv/bin/activate

pip install -r requirements.txt

docker compose up -d

uvicorn app.main:app --reload

curl -X POST http://localhost:8000/fetch