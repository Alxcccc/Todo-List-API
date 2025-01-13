from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError, NoResultFound

# Hash
import bcrypt

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
            password = self.password_hash(user.password)
            user.password = password
            new_user = User(**user.dict())
            self.session.add(new_user)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            return str(e)
        
        except ValueError as e:
            return str(e)
        
        except Exception as e:
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
            password = bytes(password, 'utf-8')
            password_hashed = bytes(result.password, 'utf-8')
            if bcrypt.checkpw(password, password_hashed):
                data = {"sub": str(result.idUsers)}
                return data
            raise ValueError("Credentials Incorrect")
        except NoResultFound as e:
            return str(e)
        
        except ValueError as e:
            return str(e)
        
    # Tasks
    
    def add_task():
        pass
        
    # Hash
    
    def password_hash(self, password: str):
        bytes_password = bytes(password, 'utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes_password, salt)
        return hashed_password