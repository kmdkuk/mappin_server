# coding: utf-8
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, Unicode, UnicodeText, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime

db = SQLAlchemy()

class CompanyAcount(db.Model):
  __tablename__ = "companyacounts"

  login_id = Column(Unicode(255), primary_key=True)
  login_password = Column(Unicode(255), nullable=False)
  company_id = Column(Integer, ForeignKey('companies.id'))

  companyacount = relationship("Company", backref=backref('companyacounts', order_by=id))

  def __init__(login_id, login_password, company_id):
    self.login_id = login_id
    self.login_password = login_password
    self.company_id = company_id

class File(db.Model):
  __tablename__ = "files"

  id = Column(Integer, primary_key=True)
  name = Column(Unicode(255), nullable=False)
  url = Column(Unicode(255))
  latitude = Column(Unicode(255)) # 緯度
  longitude = Column(Unicode(255)) # 経度
  area_radius = Column(Unicode(255))
  installation_datetime = Column(DATETIME, default=datetime.now)
  company_id = Column(Integer, ForeignKey('companies.id'))

  file = relationship("Company", backref=backref('files', order_by=id))

  def __init__(name, url, latitude, longitude, area_radius, company_id):
    self.name = name
    self.url = url
    self.latitude = latitude
    self.longitude = longitude
    self.area_radius = area_radius
    now = datetime.utcnow()
    self.company_id = company_id

class Company(db.Model):
  __tablename__ = "companies"

  id = Column(Integer, primary_key=True)
  name = Column(Unicode(255), nullable=False)
  name_kana = Column(Unicode(255), nullable=False)
  location = Column(Unicode(255), nullable=False)
  location_kana = Column(Unicode(255), nullable=False)
  responsible_person = Column(Unicode(255), nullable=False)
  responsible_person_kana = Column(Unicode(255), nullable=False)
  email = Column(Unicode(255), nullable=False)
  phone_number = Column(Unicode(255), nullable=False)

  def __init__(name, name_kana, location, location_kana, responsible_person, responsible_person_kana, email, phone_number):
    self.name = name
    self.name_kana = name_kana
    self.location = location
    self.location_kana = location_kana
    self.responsible_person
    self.responsible_person_kana = responsible_person_kana
    self.email = email
    self.phone_number = phone_number


