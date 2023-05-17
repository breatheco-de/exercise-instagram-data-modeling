import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column (String(50), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable = False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable =False)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key = True)
    Content = Column(String(140), nullable = False)
    author_id = Column(Integer, ForeignKey('follower.id'), nullable = False)


class Post (Base):
    __tablename__ = 'post'
    id= Column(Integer, primary_key = True)
    post_title = Column(String(50), nullable = False)
    post_content = Column(String(250), nullable =False)
    media_id = Column(String, ForeignKey('media.id'), nullable = True)
    comment_id = Column(String, ForeignKey('comment.id'),nullable = True)
    author_id = Column(String, ForeignKey('user.id'), nullable= False)
    like_id = Column(Integer, ForeignKey('like.id'), nullable = True)

class Media (Base):
    __tablename__ = 'media'
    id= Column(Integer, primary_key = True)
    type = Column(String(50), nullable = False)
    url = Column(String(250), nullable =False)

class like (Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key = True)
    count =Column(Integer, nullable = False)
    like_author = Column(String, ForeignKey('follower.id'), nullable = False)
    

    



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
