import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    username = Column(String(20), nullable=False)
    name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(30), nullable=False)
    followers = relationship("Followers")
    comment = relationship("Comment")
    post = relationship("Post")
    media = relationship("Media")   

class Followers(Base):
    __tablename__ = 'followers'   
    user_from_id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("Users")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    comment_text = Column(String(200), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    users = relationship("Users")    

class Post(Base):
    __tablename__ ='post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer,ForeignKey('users.id'))
    users = relationship("Users")

class Media(Base):
    __tablename__='media'
    id = Column(Integer, primary_key = True)
    type = Column(String)
    url = Column(String)
    post_id = Column(Integer, ForeignKey('post.id'))
    users = relationship("Users")
    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e