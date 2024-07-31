import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum as PyEnum

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
    followers = relationship('Follower', foreign_keys='Follower.user_to_id', backref='user_to')
    following = relationship('Follower', foreign_keys='Follower.user_from_id', backref='user_from')
    posts = relationship('Post', backref='user')

class Follower(Base):
    __tablename__ = 'Follower'
    user_from_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    
    user_from = relationship('User', foreign_keys=[user_from_id])
    user_to = relationship('User', foreign_keys=[user_to_id])

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
    
    author = relationship('User', backref='comments')
    post = relationship('Post', backref='comments')

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    
    user = relationship('User', backref='posts')
    media = relationship('Media', backref='post')

class MediaType(PyEnum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

    post = relationship('Post', backref='media')

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type.value,
            'url': self.url,
            'post_id': self.post_id
        }

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
