# Hash
import bcrypt

# Models Database
from db.models.models import Task as TaskDb
from db.models.models import User as UserDb
from models.task import Task as TaskFastapi
from models.task import TaskUpdate

# Models FastApi
from models.user import User as UserFastApi
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound, SQLAlchemyError
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:facebookalec7@localhost/todolist")


class DataBase:

    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def close_session(self):
        self.session.close()

    # Users

    def register_user(self, user: UserFastApi):
        try:
            if self.find_email(user.email):
                raise ValueError("This email registered")
            password = self.password_hash(user.password)
            user.password = password
            new_user = UserDb(**user.dict())
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

    def find_email(self, email: str):
        try:
            result = self.session.query(UserDb).filter(UserDb.email == email).one()
            return result
        except NoResultFound:
            return False

    def login(self, email, password):
        try:
            result = self.find_email(email)
            if not result:
                raise NoResultFound("This user not exist")
            password = bytes(password, "utf-8")
            password_hashed = bytes(result.password, "utf-8")
            if bcrypt.checkpw(password, password_hashed):
                data = {"sub": str(result.idUsers)}
                return data
            raise ValueError("Credentials Incorrect")
        except NoResultFound as e:
            return str(e)

        except ValueError as e:
            return str(e)

    # Tasks

    def add_task(self, id_user: int, task: TaskFastapi):
        try:
            task.idUser = id_user
            new_task = TaskDb(**task.dict())
            self.session.add(new_task)
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            self.session.rollback()
            return str(e)

        except Exception as e:
            return str(e)

    def read_tasks(self, id_user: int):
        try:
            results = self.session.query(TaskDb).filter(TaskDb.idUser == id_user).all()
            results_return = list()
            for result in results:
                results_return.append(
                    TaskFastapi(
                        idTask=result.idTask,
                        title=result.title,
                        description=result.description,
                    )
                )
            return results_return
        except SQLAlchemyError as e:
            return str(e)

        except NoResultFound as e:
            return str(e)

        except Exception as e:
            return str(e)

    def update_task(self, id_task: int, id_user: int, update: TaskUpdate):
        try:
            results = (
                self.session.query(TaskDb)
                .filter(TaskDb.idTask == id_task, TaskDb.idUser == id_user)
                .first()
            )
            if results:
                if update.title == None and update.description == None:
                    raise ValueError("The task doesn't have anything to update")
                if update.title and update.description:
                    results.title = update.title
                    results.description = update.description
                    self.session.commit()
                    return True
                if update.title:
                    results.title = update.title
                    self.session.commit()
                    return True
                results.description = update.description
                self.session.commit()
                return True
        except SQLAlchemyError as e:
            return str(e)

        except NoResultFound as e:
            return str(e)

        except Exception as e:
            return str(e)

    def delete_task(self, id_task: int, id_user: int):
        try:
            results = (
                self.session.query(TaskDb)
                .filter(TaskDb.idTask == id_task, TaskDb.idUser == id_user)
                .delete()
            )
            if results == 0:
                raise Exception("The task not exists")
            verify_delete = (
                self.session.query(TaskDb)
                .filter(TaskDb.idTask == id_task, TaskDb.idUser == id_user)
                .first()
            )
            if verify_delete:
                raise Exception("The task not delete")
            self.session.commit()
            return True
        except SQLAlchemyError as e:
            return str(e)

        except NoResultFound as e:
            return str(e)

        except Exception as e:
            return str(e)

    # Hash

    def password_hash(self, password: str):
        bytes_password = bytes(password, "utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes_password, salt)
        return hashed_password
