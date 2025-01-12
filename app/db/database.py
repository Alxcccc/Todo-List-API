from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError, NoResultFound

#Modelos FastApi
from app.models.user import User

# Modelos Database
from models import models

engine = create_engine('mysql+pymysql://root:facebookalec7@localhost/todolist')



class DataBase():
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        
    def close_session(self):
        self.session.close()
    
    def register_user(self, user: User):
        try:
            
            if self.find_duplicate_email(user.email):
                raise ValueError("This email registered")
            new_user = models.User(**user)
            self.session.add(new_user)
            self.session.commit()
            return True
        
        except SQLAlchemyError as e:
            self.session.rollback()  # Deshacer cambios si ocurre un error
            return {"error": e}
        
        except ValueError as e:
            return {"error": e}
    
    def find_duplicate_email(self, email: str):
        try:
            result = self.session.query(models.User).filter(models.User.email == email).one()
            return True
        except NoResultFound:
            return False
        
    def login(self, email, password):
        try:
            result = self.session.query(User).filter(User.email == email,User.nombre == password).one()
        except NoResultFound:
            return False
