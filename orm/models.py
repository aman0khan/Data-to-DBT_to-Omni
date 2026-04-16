"""
ORM models for the softasset_dbt project.

These models correspond to the dbt models defined in dbt_project.yml,
targeting catalog 'main' and schema 'softasset_sam_csv_final'.
"""

from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class RawSoftasset(Base):
    """
    ORM model for the raw_softasset dbt model.

    Source: main.softasset_sam_csv_final.softasset_raw
    Materialized as: table
    dbt project: softasset_dbt
    """

    __tablename__ = "raw_softasset"
    __table_args__ = {"schema": "softasset_sam_csv_final"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    asset_name = Column(String(255), nullable=False)
    asset_type = Column(String(100), nullable=True)
    version = Column(String(50), nullable=True)
    license_type = Column(String(100), nullable=True)
    vendor = Column(String(255), nullable=True)
    purchase_date = Column(DateTime, nullable=True)
    expiry_date = Column(DateTime, nullable=True)
    cost = Column(Float, nullable=True)
    status = Column(String(50), nullable=True)
    assigned_to = Column(String(255), nullable=True)
    department = Column(String(100), nullable=True)
    notes = Column(Text, nullable=True)


# Project-level metadata matching dbt_project.yml
DBT_PROJECT_NAME = "softasset_dbt"
DBT_PROJECT_VERSION = "1.0.0"
DBT_CATALOG = "main"
DBT_SCHEMA = "softasset_sam_csv_final"
DBT_MATERIALIZED = "table"
