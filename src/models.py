import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

#Trabajo en equipo con Daniel Carrion, Sergio Reverte e Inti Luna

Base = declarative_base()

followers = Table('followers',
Base.metadata,
Column('follower_id', Integer, ForeignKey('follower.id'), primary_key=True),
Column('user_id ', Integer, ForeignKey('user.id'), primary_key=True)
)

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
   

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(250), nullable=True)
    firstname = Column(String(250), nullable=True)
    lastname = Column(String(250), nullable=True)
    email = Column(String(250), nullable=True)
    #nuevos atributos de proyecto final
    direccion = Column(String(120), unique=False, nullable=False)
    telefono = Column(Integer, unique=True, nullable=False)
    codigo_postal = Column(Integer, unique=False, nullable=False)
    comunidad_autonoma_id = Column(Integer, ForeignKey('comunidades_autonomas.id'),nullable=False)
    provincia_id = Column(Integer, ForeignKey('provincias.id'),nullable=False)

    posts = relationship('Post', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)
    followers = relationship('Follower', secondary= followers, lazy='subquery',
        backref= backref('users', lazy=True))
   

    def to_dict(self):
        return {}
    
#tablas de proyecto
class ComunidadAutonoma(Base):
    __tablename__ = 'comunidades_autonomas'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    user = relationship('User', backref='comunidades_autonomas', lazy=True)
    provincia = relationship('Provincia', backref='comunidades_autonomas', lazy=True)

    def to_dict(self):
        return {}
    
class Provincia(Base):
    __tablename__ = 'provincias'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    user = relationship('User', backref='provincias', lazy=True)
    comunidad_autonoma_id = Column(Integer, ForeignKey('comunidades_autonomas.id'),nullable=False)

    def to_dict(self):
        return {}

class PerfilProductor(Base):
    __tablename__ = 'perfil_productores'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    #user_id =
    nombre_huerta = Column(String(250), nullable=True)
    foto_portada = Column(String(250), nullable=True)
    foto_perfil = Column(String(250), nullable=True)
    problemas = Column(String(250), nullable=True)
    donde_encontrar = Column(String(250), nullable=True)
    latitud = Column(String(250), nullable=True)
    longitud = Column(String(250), nullable=True)


    # comunidad_autonoma_id = Column(Integer, ForeignKey('comunidades_autonomas.id'),nullable=False)
    # provincia_id = Column(Integer, ForeignKey('provincias.id'),nullable=False)

    # posts = relationship('Post', backref='user', lazy=True)
    # comments = relationship('Comment', backref='user', lazy=True)
    # followers = relationship('Follower', secondary= followers, lazy='subquery',
    #     backref= backref('users', lazy=True))
   

    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, nullable=False, primary_key=True)
    type = Column(String(250), nullable=True)
    url = Column(String(250), nullable=True)
    post_id = Column(Integer, ForeignKey('post.id'),
        nullable=False)

    def to_dict(self):
        return {}
    

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    medias = relationship('Media', backref='post', lazy=True)
    comments = relationship('Comment', backref='post', lazy=True)



    def to_dict(self):
        return {}
    
class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, nullable=False, primary_key=True)
    comment_text = Column(String(250), nullable=True)
    author_id = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'),
        nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e