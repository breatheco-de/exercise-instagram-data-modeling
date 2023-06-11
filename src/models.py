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
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    number_phone = Column(String(20), nullable=False)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    post = relationship('Post',back_populates='users', uselist=True)
    reel = relationship('Reel',back_populates='users', uselist=True)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    img = Column(String(250), nullable=False) 
    caption = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship('Comment',back_populates='posts', uselist=True)
    reaction = relationship('Reaction',back_populates='posts', uselist=True)

class Reel(Base):
    __tablename__ = 'reels'
    id = Column(Integer, primary_key=True)
    video = Column(String(250), nullable=False)
    caption = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship('Comment',back_populates='posts', uselist=True)
    reaction = relationship('Reaction',back_populates='posts', uselist=True)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Reaction(Base):
    __tablename__ = 'reactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) 
    post_id = Column(Integer, ForeignKey('post.id'))   

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
