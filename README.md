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

## Activate the virtual env and install dependencies:

```bash
python3 -m venv .tecvenv

source .venv/bin/activate

pip install -r requirements.txt
```

## Configure the PostgreSQL Database. 
 Either create a '.env' file containing this URL: 
```DATABASE_URL=postgresql://chenard612:eiPI10LE170&@localhost:5433/tec_energy_db```

Alternatively, you can change the values directly inside the **'db.py'** file in order to correspond to the information contained inside the **'docker.compose.yml'** file.
Then, please run the following command. It should run the database in a docker container.

```bash
docker compose up -d
```

## Run the server with this command:

```bash
uvicorn app.main:app --reload
```

## Run the Query
Run this curl inside the command line to trigger the query of the CSV, its parsing and its insertion in the database.

```bash
curl -X POST http://localhost:8000/fetch
```

## OPTIONAL: 
To automate the query of the CSV, please uncomment the code contained inside **'scheduler.py'**. By default, the query is scheduled to run every 6 hours, but it has been disabled to allow a manual trigger.