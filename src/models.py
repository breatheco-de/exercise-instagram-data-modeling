import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name=Column(String(100), nullable=False)
    last_name=Column(String(100), nullable=False )
    email=Column(String(100), nullable=False)

class Follower(Base):
    __tablename__= 'follower'
    user_from_id=Column(Integer, primary_key= True)
    user_to_id= Column(Integer, ForeignKey('user.id'))
    user= relationship(User)   
  
class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))
    #user = relationship(User)
    #post= relationship(Post)

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__= 'post'
    id= Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))

class Media(Base):
    __tablename__= 'media'
    id= Column(Integer, primary_key=True)
    url= Column(String(100), nullable=False)       
    post_id= Column(Integer, ForeignKey('post.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')