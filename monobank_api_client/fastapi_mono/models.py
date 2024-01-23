from datetime import datetime
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MonoModel(Base):
    __tablename__ = "mono"

    id = Column(Integer, primary_key=True, unique=True)
    mono_token = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    user_id = Column(String, unique=True, nullable=False)
