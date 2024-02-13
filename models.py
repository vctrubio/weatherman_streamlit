from pydantic import BaseModel
from typing import List, Optional
from dataclasses import field
from dbs import Base

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session, sessionmaker


class Location(BaseModel):
    latitude: float = 0
    longitude: float = 0
    address: str = field(default=None)
    days: List['Day']

    def print_all_days(self):
        for day in self.days:
            print(day)
        
class LocationDB(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    # unique doesnt do shit
    address = Column(String, nullable=False, unique=True)
    days = relationship('DayDB', back_populates='location')

    def print_days(self):
        print(f'Address: {self.address}: Days: {len(self.days)}')
        for day in self.days:
            day.print_attributes()

class Day(BaseModel):
    datetime: str
    feelslike: float
    tempmin: float
    tempmax: float
    precip: float
    precipprob: int
    conditions: str
    moonphase: float
    
    def __repr__(self) -> str:
        return 'this is a test'


class DayDB(Base):
    __tablename__ = 'days'

    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(String)
    conditions = Column(String, nullable=True)
    feelslike = Column(Float)
    tempmin = Column(Float)
    tempmax = Column(Float)
    precip = Column(Float, nullable=True)
    precipprob = Column(Integer, nullable=True)
    moonphase = Column(Float, nullable=True)
    location_id = Column(Integer, ForeignKey('locations.id'))
    location = relationship('LocationDB', back_populates='days')

    def print_attributes(self):
        attributes = [f'{attr}: {value}' for attr,
                      value in self.__dict__.items() if not attr.startswith('_')]
        print(', '.join(attributes))
