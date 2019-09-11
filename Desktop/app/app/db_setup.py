import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Date,DateTime,Boolean,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import UserMixin
import datetime
from sqlalchemy.sql.expression import func



Base = declarative_base()





#Questions table 


class Question(Base):
	__tablename__='question'
	

	id=Column(Integer,primary_key=True)
	text=Column(String(140),nullable=False)
	tags=Column(String(100),nullable=True)
	created_at = Column(DateTime, default=datetime.datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.datetime.utcnow)
    
#Poll Response table
class PollResponse(Base):
	__tablename__='poll_response'

	id=Column(Integer,primary_key=True)
	q_id=Column(Integer,ForeignKey('question.id'))  
	opt=Column(String(100),nullable=False)
	op=Column(Integer)
	question=relationship(Question)
#Response table
class Response(Base):
	__tablename__='response'

	id=Column(Integer,primary_key=True)
	qid=Column(Integer,ForeignKey('question.id'))
	userid=Column(Integer,ForeignKey('users.id'))
	created_at = Column(DateTime, default=datetime.datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.datetime.utcnow)
#Users table
class User(Base,UserMixin):
	__tablename__='users'

	id = Column(Integer, primary_key=True)
	
	email=Column(String(100),unique=True,nullable=False)
	name=Column(String(100),nullable=True)
	avatar=Column(String(200))
	active=Column(Boolean,default=False)
	tokens=Column(Text)
	created_at = Column(DateTime, default=datetime.datetime.utcnow)
engine = create_engine('sqlite:///poll.db')


Base.metadata.create_all(engine)

		
		


