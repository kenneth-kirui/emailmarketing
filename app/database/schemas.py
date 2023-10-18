
from pydantic import BaseModel
from datetime import datetime

class Tamplate(BaseModel):
    name: str
    date_created: datetime
    data: str

    class Config:
        orm_mode = True


class CreateTamplate(Tamplate):
    pass

class User(BaseModel):
    fname: str
    sname:str
    username:str
    password:str
    date_created: datetime
    org_id: int
    phone_number:int
    email:str
    
    class Config:
        orm_mode = True

class CreateUser(User):
    pass

class Organization(BaseModel):
    name: str
    date_created:datetime

    class Config:
        orm_mode = True

class CreateOrganization(Organization):
    pass

class EmailAdress(BaseModel):
    date_created: datetime
    name:str
    email:str

    class Config:
        orm_mode = True

class createEmailAdress(EmailAdress):
    pass
