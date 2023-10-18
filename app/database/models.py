from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base

class Template(Base):
    __tablename__ = "template"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    date_created = Column(DateTime, nullable=False)
    data = Column(String, nullable=False)

     #Relationship
   # outboxes= relationship("Outbox", back_populates="template")
    outboxes = relationship("Outbox", back_populates="template")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    fname = Column(String, nullable=False)
    sname= Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column (String, nullable=False)
    date_created = Column(DateTime, nullable=False)
    org_id = Column(Integer, ForeignKey("organization.id"), nullable=False)
    phone_number = Column(String)
    email = Column(String)

    #Relationship
    organizations= relationship("Organization", back_populates="users")
    outboxes = relationship("Outbox", back_populates="users")
   

class Outbox(Base):
    __tablename__ = "outbox"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date_created = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    template_id= Column(Integer, ForeignKey("template.id"))
    email_address = Column(Integer, ForeignKey("emailAddress.id"))
    organization = Column(Integer, ForeignKey("organization.id"))
    status = Column(Integer, ForeignKey("status.id"))

    #Relationship
    emailAddresses = relationship("EmailAdress", back_populates="outboxes")
    #tamplates= relationship("Template", back_populates="outboxes")
    template = relationship("Template", back_populates="outboxes")
    users = relationship("User", back_populates="outboxes")
    statuses= relationship("Status", back_populates="outboxes")
    organizations = relationship("Organization", back_populates="outboxes")

class EmailAdress(Base):
    __tablename__ = "emailAddress"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date_created = Column(DateTime)
    name = Column(String)#individual or organization name
    email = Column(String)

    #Relationship
    outboxes = relationship("Outbox", back_populates="emailAddresses")
    
class Status(Base):
    __tablename__= "status"

    id  = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String)# represent the statuses of emails sent e.g delivered, sent etc.
    
    #Relationship
    outboxes = relationship("Outbox", back_populates="statuses")

class Organization(Base):
    __tablename__= "organization"

    id  = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date_created = Column(DateTime, nullable = False)
    name = Column (String)

     #Relationship
    users= relationship("User", back_populates="organizations")
    subscribers = relationship("Subscriber", back_populates="organizations")
    outboxes = relationship("Outbox", back_populates="organizations")

class Subscriber(Base):
    __tablename__= "subscriber"

    id  = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date_created = Column(DateTime)
    email_address = Column(String)
    organization = Column(Integer, ForeignKey("organization.id"))

     #Relationship
    organizations= relationship("Organization", back_populates="subscribers")





