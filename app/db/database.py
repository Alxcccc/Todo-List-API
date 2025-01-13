from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError, NoResultFound

# Models FastApi
from models.user import User
from models.task import Task

# Models Database
from db.models.models import User

engine = create_engine('mysql+pymysql://root:facebookalec7@localhost/todolist')


class DataBase():
    
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        
    def close_session(self):
        self.session.close()
    
    # Users
    def register_user(self, user: User):
        try:
            if self.find_duplicate_email(user.email):
                raise ValueError("This email registered")
            new_user = User(**user.dict())
            self.session.add(new_user)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            return str(e)
        
        except ValueError as e:
            return str(e)
    
    def find_duplicate_email(self, email: str):
        try:
            self.session.query(User).filter(User.email == email).one()
            return True
        except NoResultFound as e:
            return False
        
    def login(self, email, password):
        try:
            result = self.session.query(User).filter(User.email == email).one()
            if not result:
                raise NoResultFound("This user not exist")
            if result.password == password:
                return True
            raise ValueError("Credentials Incorrect")
        except NoResultFound as e:
            return str(e)
        
        except ValueError as e:
            return str(e)

    # Tasks
    
    def add_task():
        pass