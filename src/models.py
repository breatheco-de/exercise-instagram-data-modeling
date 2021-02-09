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
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    firstName = Column(String(25), nullable=False)
    lastName = Column(String(25), nullable=False)
    email = Column(String(40), nullable=False)
    bio = Column(String(280), nullable=False)
class Followers(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(280), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    liked_by_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    itsType = Column(String(280), nullable=False)
    itsurl = Column(String(280), nullable=False)
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    media_id = Column(Integer, ForeignKey('media.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    liked_by_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    media = relationship(Media)
class Reel(Base):
    __tablename__ = 'reel'
    id = Column(Integer, primary_key=True)
    media_id = Column(Integer, ForeignKey('media.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    liked_by_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    media = relationship(Media)
class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    media_id = Column(Integer, ForeignKey('media.id'))
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    media = relationship(Media)
    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
