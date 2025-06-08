from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Energy_Transfer(Base):
    __tablename__ = "energy_transfer"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(TIMESTAMP, server_default=func.now())
    location = Column(Integer)
    location_zone = Column(String)
    location_name = Column(String)
    location_quantity = Column(String)
    location_purpose_description = Column(String)
    flow_indicator = Column(String)
    design_capacity = Column(Integer)
    operating_capacity = Column(Integer)
    total_scheduled_quantity = Column(Integer)
    operational_available_capacity = Column(Integer)
    it_indicator = Column(Boolean)
    auth_overrun_indicator = Column(Boolean)
    nomination_capacity_exceeded = Column(Boolean)
    all_quantity_available = Column(Boolean)
    quantity_reason = Column(String)
