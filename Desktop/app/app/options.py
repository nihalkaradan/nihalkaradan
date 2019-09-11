from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Question, Base, PollResponse,User

engine = create_engine('sqlite:///poll.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

question1 = Question(text="Urban Burger")

session.add(question1)
session.commit()

option1 = PollResponse(opt="French Fries",question=question1,op=0) 
                                        
session.add(option1)
session.commit()



option2 = PollResponse(opt="French Fries2",question=question1,op=0) 
                                        
session.add(option2)
session.commit()



option3 = PollResponse(opt="French Fries3",question=question1,op=0) 
                                        
session.add(option3)
session.commit()

option4 = PollResponse(opt="French Fries4",question=question1,op=0) 
                                        
session.add(option4)
session.commit()

option5 = PollResponse(opt="other",question=question1,op=0) 
                                        
session.add(option5)
session.commit()
user1=User(email='nk@a.com',name='nihal')
session.add(user1)
session.commit()


print "added option items!"