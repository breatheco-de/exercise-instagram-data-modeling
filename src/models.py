import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250),nullable=False)
    password = Column (String(250),nullable=False)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('users.id'),nullable=False)
    user = relationship ('User')
    url = Column (String(250),nullable=False)
    description = Column (String(250),nullable=False)

class Like(Base):
    __tablename__='likes'
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('users.id'),nullable=False)
    user = relationship ('User')
    post_id = Column (Integer, ForeignKey('posts.id'),nullable=False)
    post = relationship(Post)
    description = Column (String (500),nullable=False)

class Follower (Base):
    __tablename__='followers'
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('users.id'),nullable=False)
    user_follower = Column (Integer, ForeignKey('users.id'),nullable=False)
    user = relationship ('User')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
