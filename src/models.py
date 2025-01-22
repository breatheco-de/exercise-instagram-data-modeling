import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

# Tabla Usuario
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(200), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    biografia = Column(String(500))
    foto_perfil = Column(String(200))

    posts = relationship('Post', backref='usuario', lazy=True)
    comentarios = relationship('Comentario', backref='usuario', lazy=True)
    seguidores = relationship('Seguidor', backref='seguidor', lazy=True)

    def __repr__(self):
        return f'<Usuario {self.nombre}>'

# Tabla Post
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    titulo = Column(String(100), nullable=False)
    contenido = Column(String(500))
    fecha_publicacion = Column(DateTime, default=datetime.utcnow)
    imagen = Column(String(200))
    likes = Column(Integer, default=0)

    comentarios = relationship('Comentario', backref='post', lazy=True)

    def __repr__(self):
        return f'<Post {self.titulo}>'

# Tabla Comentario
class Comentario(Base):
    __tablename__ = 'comentario'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    contenido = Column(String(500), nullable=False)
    fecha_comentario = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Comentario {self.id}>'

# Tabla Seguidor
class Seguidor(Base):
    __tablename__ = 'seguidor'
    id = Column(Integer, primary_key=True)
    seguidor_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    seguido_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)

    def __repr__(self):
        return f'<Seguidor {self.seguidor_id} sigue a {self.seguido_id}>'

# Crear las tablas en la base de datos
engine = create_engine('sqlite:///instagram_clone.db')
Base.metadata.create_all(engine)

# Generar diagrama con ERAlchemy
try:
    result = render_er(Base, 'diagram.png')
    print("¡Éxito! Revisa el archivo diagram.png")
except Exception as e:
    print("Hubo un problema al generar el diagrama")
    raise e
