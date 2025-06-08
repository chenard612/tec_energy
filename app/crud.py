from app.db import SessionLocal
from app.models import Energy_Transfer

def save_energy_transfers(data: list[dict]):
    db = SessionLocal()
    try:
        for item in data:
            db.add(Energy_Transfer(**item))
        db.commit()
        print(f"Inserted {len(data)} entries.")
    except Exception as e:
        db.rollback()
        print(f"Failed to insert entries: {e}")
    finally:
        db.close()