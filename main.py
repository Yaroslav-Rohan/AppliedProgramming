import os
from sqlalchemy import orm, create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URI = os.getenv("DB_URI", "postgresql://postgres:1234@localhost:5432/postgres")
engine = create_engine(DB_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    uid = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)

class Auditorium(Base):
    __tablename__ = 'auditorium'
    uid = Column(Integer, primary_key=True)
    number = Column(String)

class Booking(Base):
    __tablename__ = 'booking'
    uid = Column(Integer, primary_key=True)
    user_uid = Column(Integer, ForeignKey(Users.uid))
    auditorium_uid = Column(Integer, ForeignKey(Auditorium.uid))
    auditorium_status = Column(String)
    booking_date_start = Column(DateTime)
    booking_date_final = Column(DateTime)

    from_user = orm.relationship(
        Users, backref="booking", lazy="joined"
    )
    from_auditorium = orm.relationship(
        Auditorium, backref="booking", lazy="joined"
    )
