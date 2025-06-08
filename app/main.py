from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.scheduler import start_scheduler
from app.api import query_csv
from app.db import init_db



@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()     
    start_scheduler()
    yield
    
app = FastAPI(title="Tec Energy Interview Exercise", lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Query functional."}

@app.post("/fetch")
def trigger_csv_fetch():
    try:
        query_csv()
        return {"status": "success", "message": "CSV data fetched and processed."}
    except Exception as e:
        return {"status": "error", "message": str(e)}