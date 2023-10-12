import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = relationship("Address", uselist=False, backref="person")

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship("Person", backref="address")

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    users = relationship('User', backref='follower')

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))
    follower_id = Column(Integer, ForeignKey('follower.id'), nullable=False)
    follower = relationship("Follower", backref="users")
    media = relationship("Media", backref="user")

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref="media")
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", backref="media")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref="posts")
    media = relationship("Media", backref="post")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    author = relationship("User", backref="comments")
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship("Post", backref="comments")

def to_dict(self):
    return {}

# Dibuja el diagrama ER
try:
    result = render_er(Base, 'diagram.png')
    print("¡Éxito! Consulta el archivo diagram.png")
except Exception as e:
    print("Hubo un problema al generar el diagrama")
    raise e
