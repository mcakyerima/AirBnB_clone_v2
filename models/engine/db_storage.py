#!/usr/bin/python3
'''
Define class DatabaseStorage
'''
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.base_model import Base


class DBStorage:
    '''
    Create SQLAlchemy database
    '''

    __engine = None
    __session = None

    def __init__(self):
        '''
        Create engine and link to MySQL database (hbnb_dev, hbnb_dev_db)
        '''
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        Query current database session
        If cls is provided, filter instances based on the class name.
        '''
        db_dict = {}

        if cls and isinstance(cls, str):
            objs = self.__session.query(models.classes[cls]).all()
        elif cls:
            objs = self.__session.query(cls).all()
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    if objs:
                        for obj in objs:
                            key = f"{obj.__class__.__name__}.{obj.id}"
                            db_dict[key] = obj
            return db_dict

    def new(self, obj):
        '''
        Add object to the current database session.
        '''
        self.__session.add(obj)

    def save(self):
        '''
        Commit all changes of the current database session.
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Delete from the current database session.
        '''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''
        Commit all changes of the current database session.
        '''
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        '''
        Close the current database session.
        '''
        self.__session.close()
