from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    additional_info = Column(String, nullable=False)