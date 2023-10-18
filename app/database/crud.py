from sqlalchemy.orm import Session

from . import models, schemas


def get_template(db: Session, template_id: int):
    return db.query(models.Template).filter(models.template.id == template_id).first()

def create_template(db: Session, template: schemas.Tamplate):
    db_template = models.Template(name=template.name, data = template.data)
    db.add(db_template)
    db.commit()
    db.refresh(db_template)
    return db_template

def create_template_data(db: Session, data: schemas.CreateTamplate):
    db_item = models.Template(**data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#creating user
def create_user_data(db:Session, data:schemas.CreateUser):
    db_user = models.User(**data.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# crud function to create organizations
def create_organization_data(db:Session, data:schemas.CreateOrganization):
    db_organization = models.Organization(**data.dict())
    db.add(db_organization) 
    db.commit()
    db.refresh(db_organization)
    return db_organization

# crude to add email address to the email contact lis

def create_emailaddress_data(db:Session, data:schemas.createEmailAdress):
    db_emailaddress = models.EmailAdress(**data.dict())
    db.add(db_emailaddress)
    db.commit()
    db.refresh(db_emailaddress)
    return db_emailaddress