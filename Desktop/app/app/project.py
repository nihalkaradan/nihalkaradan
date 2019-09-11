from flask import Flask, render_template, request, redirect, url_for, jsonify,make_response,Session,Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import flask_login
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from db_setup import Base,Question,PollResponse,Response,User
from sqlalchemy.sql import exists
from urlparse import urlparse, urljoin
pid=None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecret'
engine = create_engine('sqlite:///poll.db')
Base.metadata.bind = engine
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
activity=False



@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login?next=' + request.path)
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
def get_redirect_target():
    for target in request.values.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target
def redirect_back(endpoint, **values):
    target = request.form['next']
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)
@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out!'

@app.route('/')
def index():
	return render_template('signup1.html')



@app.route('/login',methods=['GET','POST'])
def login():
    next = get_redirect_target()
    pid=None
    if request.method=='POST':
        email1=request.form['email']
        name1=request.form['name']
        

        if session.query(exists().where(User.email==email1)).scalar():
            uk=session.query(User).filter_by(email=email1).one()
            if name1==uk.name :
                global pid
                pid=uk.id
                if uk.active==False:
                    global pid
                    pid=uk.id
                    login_user(uk)
                    return redirect_back('newpoll')
                else:
                    global pid
                    pid=uk.id
                    login_user(uk)
                    return redirect_back('newpoll')
                
            else:
                return render_template('signup1.html',next=next)
        else:
            uk=User(email=email1,name=name1)

            session.add(uk)
            session.commit()
            global pid
            pid=uk.id
            login_user(uk)
            return redirect_back('newpoll')
        
    return render_template ('signup1.html',next=next)
"""@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email1=request.form['email']
        name1=request.form['name']
        
        if session.query(exists().where(User.email==email1)).scalar():
            uk=session.query(User).filter_by(email=email1).one()
            if name1==uk.name :
                login_user(uk)
            return 'user already exist'
        else:
            user1=User(email=email1,name=name1)
            session.add(user1)
            session.commit()
            login_user(user1)
    return render_template('signup1.html')"""


@app.route('/question/<int:q_id>/')
def options(q_id):
	question=session.query(Question).filter_by(id=q_id).one()
	items=session.query(PollResponse).filter_by(q_id=q_id).all()

	return render_template('poll.html',question=question,items=items,next=next)

@app.route('/question/<int:q_id>/newpoll', methods=['GET', 'POST'])
@login_required
def newpoll(q_id):
    
    
	question=session.query(Question).filter_by(id=q_id).one()
	items=session.query(PollResponse).filter_by(q_id=q_id).all()
  
	editedItem=session.query(PollResponse).filter_by(q_id=q_id).all()

	if request.method == 'GET' and current_user.active==False:
		if request.args.get('id'):
			eid=request.args.get('id')
			editedItem=session.query(PollResponse).filter_by(id=eid).one()
			editedItem.op=editedItem.op+1

		session.add(editedItem)
    	session.commit()
        user=session.query(User).filter_by(id=current_user.id).one()
        current_user.active=True
        user.active=True
        session.add(user)
        session.commit()
        return render_template('graph.html',question=question,items=items)

    
    

	
			
#function for new polling

"""@app.route('/question/<int:q_id>/newpoll', methods=['GET', 'POST'])
def newpoll(q_id):
	#question=session.query(Question).filter_by(id=q_id).one()

	#if request.method == 'POST':
    #	if request.form['radio']:
	#		newPoll = session.query(PollResponse).filter_by(id=request.form['radio']).one()
    #    	newPoll.op = newPoll.op+1
    if request.method == 'POST':
    	editedItem = session.query(PollResponse).filter_by(id=int(request.form['radio'])).one()
        if request.form['radio']:
        	
			editedItem.op = editedItem.op+1
        session.add(editedItem)
        session.commit()
        return redirect(url_for('options', q_id=q_id))
    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU
        # SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template(
            'poll.html', q_id=restaurant_id, pollresponse_id=pollresponse_id, item=editedItem)"""

DBSession = sessionmaker(bind=engine)
session = DBSession()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
