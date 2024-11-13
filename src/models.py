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
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False, unique=True)


class Posts(Base):
    __tablename__='posts'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('Users')

    def to_dict(self):
        return {}

class Medias(Base):
    __tablename__='medias'
    id = Column(Integer, primary_key=True)
    type = Column (String(300), nullable=False)
    media = Column (String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'))
    posts = relationship('Posts')


class Comments(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    author = relationship('User', foreign_keys=['users_id'])
    post = relationship('Posts', foreign_keys=['posts_id'])


class Followers(Base):
    __tablename__='followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('users.id'))
    user_to_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', foreign_keys=['users_id'])
    user = relationship('User', foreign_keys=['users_id'])


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
