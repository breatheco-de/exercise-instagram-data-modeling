import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    number_phone = Column(String(20), nullable=False)
    country = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    posts = relationship('Post', back_populates='user')
    reels = relationship('Reel', back_populates='user')
    comments = relationship('Comment', back_populates='user')


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    caption = Column(String(500), nullable=False)
    image_url = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False)
    user = relationship('User', back_populates='posts')
    reactions = relationship('Reaction', back_populates='post')
    comments = relationship('Comment', back_populates='post')


class Reel(Base):
    __tablename__ = 'reels'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    video_url = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False)
    user = relationship('User', back_populates='reels')
    reactions = relationship('Reaction', back_populates='reel')
    comments = relationship('Comment', back_populates='reel')


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    reel_id = Column(Integer, ForeignKey('reels.id'))
    content = Column(String(500), nullable=False)
    created_at = Column(DateTime, nullable=False)
    user = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')
    reel = relationship('Reel', back_populates='comments')


class Reaction(Base):
    __tablename__ = 'reactions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    reel_id = Column(Integer, ForeignKey('reels.id'))
    reaction_type = Column(String(20), nullable=False)
    user = relationship('User')
    post = relationship('Post')
    reel = relationship('Reel')

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
