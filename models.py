# coding: utf-8
from sqlalchemy import Column, Date, MetaData, String, Table, Time

metadata = MetaData()


t_policedata = Table(
    'policedata', metadata,
    Column('date', Date, nullable=False),
    Column('time', Time, nullable=False),
    Column('service_area', String(20), nullable=False),
    Column('subject_age', String(20), nullable=False),
    Column('subject_race', String(50), nullable=False),
    Column('subject_sex', String(50), nullable=False),
    Column('arrest_made', String(20), nullable=False),
    Column('citation_issued', String(20), nullable=False),
    Column('warning_issued', String(20), nullable=False),
    Column('outcome', String(20), nullable=False)
)
