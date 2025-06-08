import csv
from io import StringIO
from datetime import datetime
from app.crud import save_energy_transfers

def to_bool(value: str) -> bool:
    return value.strip().upper() == "Y"

def parse_csv_file(csv_content):
    reader = csv.DictReader(StringIO(csv_content))
    valid_rows = []
    for row in reader:
        try:
            energy_transfer = {
                "timestamp": datetime.now(),
                "location": row["Loc"],
                "location_zone": row["Loc Zn"],
                "location_name": row["Loc Name"],
                "location_quantity": row["Loc/QTI"],
                "location_purpose_description": row["Loc Purp Desc"],
                "flow_indicator": row["Flow Ind"],
                "design_capacity": int(row["DC"]),
                "operating_capacity": int(row["OPC"]),
                "total_scheduled_quantity": int(row["TSQ"]),
                "operational_available_capacity": int(row["OAC"]),
                "it_indicator": to_bool(row["IT"]),
                "auth_overrun_indicator": to_bool(row["Auth Overrun Ind"]),
                "nomination_capacity_exceeded": to_bool(row["Nom Cap Exceed Ind"]),
                "all_quantity_available": to_bool(row["All Qty Avail"]),
                "quantity_reason": row['Qty Reason']
            }
            valid_rows.append(energy_transfer)
        except Exception as e:
            print(f"Skipping row: {e}")
    save_energy_transfers(valid_rows)