import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=True)
    email = Column(String(100), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey=True)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(150), nullable=False)
    author_id = Column(Integer, ForeignKey=True)
    post_id = Column(Integer, ForeignKey=True)

class Medias(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    type = Column(Enum, nullable=False)
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey=True)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey=True)
    user_to_id = Column(Integer, ForeignKey=True)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
