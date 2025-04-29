from db.connection import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, DateTime

class EmailStore(Base):
    __tablename__ = "email_store"
    id = Column(Integer, primary_key=True)
    email_id = Column(String(256), unique=True)
    username = Column(String(128))
    domain_name = Column(String(128))
    received_date = Column(DateTime)
    created_date = Column(DateTime)