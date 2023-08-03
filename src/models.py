import os
import sys
from sqlalchemy import Column,Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    firstname = Column(String(64), nullable=False)
    lastname = Column(String(64), nullable=False)

class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user_to_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship(User)
 
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type = Column(Enum("image", "video", "audio"))
    url = Column(String(50))
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    post = relationship(Post)

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(2200), nullable=False)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    user = relationship(User)
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
