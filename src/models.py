import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum as SQLEnum 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum

Base = declarative_base()

    
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

     # Booleanos
    is_banned = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    # Relationships
    followers = relationship("Follower", backref="user_followers") # Referencia a la relacion
    comments = relationship("Comment", backref="user_comments")
    posts = relationship("Post", backref="user_posts")
    
class Follower(Base):
    __tablename__ = "follower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))


    # Relationship
    user = relationship(User)
    

class Comment(Base):
     __tablename__ = "comment"
     id = Column(Integer, primary_key=True)
     comment_text = Column(String(100), nullable=False )
     author_id = Column(Integer, ForeignKey("user.id"))
     post_id = Column(Integer, ForeignKey("post.id"))


# Relationship
    
class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))

# Relationship
    post = relationship("Post", backref="comment_post")
    media = relationship("Media", backref="post_media")


class MediaType(Enum):
    PHOTO = "photo"
    VIDEO = "video"

class Media(Base):
     __tablename__ = "media"
     id = Column(Integer, primary_key=True)
     type = Column(SQLEnum(MediaType), nullable=False)
     url = Column(String(100), nullable=False)
     post_id = Column(Integer, ForeignKey("post.id"))


    # Relationship
     post = relationship(Post)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
