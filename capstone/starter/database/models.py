from csv import list_dialects
from platform import release
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
import os 



#migrate = Migrate(app, db)

database_path = 'postgresql://postgres@localhost:5432/agency'

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'Movies data model'
class Movies(db.Model):
    __tablename__= 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    release_year = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    
    def __repr__(self):
        return f"movies {self.id} name: {self.title}"
    
    def __init__(self, title, release_year, duration):
        self.title = title    
        self.release_year = release_year
        self.duration = duration
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'duration': self.duration 
        }
        
    
'Actors data model'
class Actors(db.Model):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    
    
    def __repr__(self):
        return f"actors {self.id} name {self.name}"
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender
        

    def insert(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender 
        }
        
        
        

    