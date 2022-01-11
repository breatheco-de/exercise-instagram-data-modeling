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
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    posts = relationship("Post", backref="poster")
    followers = relationship("Follower", backref="followed")

    def __repr__(self):
        return f"User #{self.id}: {self.username}"

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    creator = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(String(50), nullable=False)
    image = Column(String(150), nullable=False)
    description = Column(String(300))
    comments = relationship("Comment", backref="commented_post")

    def __repr__(self):
        return f"#{self.id}: {self.title} | {self.description}"

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    comment = Column(String(300), nullable=False)
    
    def __repr__(self):
        return f"User #{self.user.id} commented on post #{self.post_id}: {self.comment}"


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    follower = Column(Integer, ForeignKey("user.id"))
    following = Column(Integer, ForeignKey("user.id"))
    
    def __repr__(self):
        return f"User #{self.follower} is following {self.following}"

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e