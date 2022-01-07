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
    id = Column(Integer, primary_key = True)
    userName = Column(String(50), nullable = False)
    firstName = Column(String(50), nullable = False)
    lastName = Column(String(50), nullable = False)
    email = Column(String(50), nullable = False, unique=True)

    followers = relationship('Follower')
    comments = relationship('Comment')
    post = relationship('Post')

class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    image_url = Column(String(250))
    comments = Column(String(250))
    likes = Column(Integer)
    media = relationship('Media')
    comments = relationship('Comment')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable = False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))


class Media(Base):
    __tablename__='media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250), nullable = False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Follower(Base):
    __tablename__='follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')