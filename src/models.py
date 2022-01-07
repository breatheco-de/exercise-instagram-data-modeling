import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)
    
  
class Post(Base):
    __tablename__='Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column(String(250))
    comments = Column(String(250))
    likes = Column(Integer)
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)


class Media(Base):
    __tablename__='Media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

class Follower(Base):
    __tablename__='Follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')