import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


# Creamos una instancia de Base de SQLAlchemy para declarar modelos
Base = declarative_base()

# Definición del modelo User
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    posts = relationship("Post", backref="user", cascade="all, delete-orphan")
    followers = relationship("Follow", foreign_keys="Follow.followed_id", backref="followed")
    following = relationship("Follow", foreign_keys="Follow.follower_id", backref="follower")

# Definición del modelo Post
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    image_url = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

# Definición del modelo Follow
class Follow(Base):
    __tablename__ = 'follows'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('users.id'))
    followed_id = Column(Integer, ForeignKey('users.id'))

# Definición del modelo Comment
class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

# Draw from SQLAlchemy base. Generación del diagrama UML usando eralchemy2 y la instancia de Base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

# Terminal for diagram.png
# pipenv shell
# pip install sqlalchemy
# python3 src/models.py