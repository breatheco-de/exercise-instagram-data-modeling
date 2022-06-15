import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(150))
    firstname = Column(String(100))
    lastname = Column(String(100))
    email = Column(String(80))
    post = relationship('Post', backref="user")
    media = relationship('Media', backref="user")
    comment = relationship('Comment', backref="user")
    follower = relationship('Follower', backref="user")

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post = relationship('Post', backref="user")


class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey("post.id"))
    media = relationship('Media', backref="user")


class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    comment = relationship('Comment', backref="user")


class Follower(Base):
    __tablename__ = "follower"
    user_from_id = Column(Integer, ForeignKey("user.id"),primary_key=True)
    user_to_id = Column(Integer, ForeignKey("user.id"),primary_key=True)
    follower = relationship('Follower', backref="user")



def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')