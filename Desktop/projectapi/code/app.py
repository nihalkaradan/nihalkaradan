from flask import Flask
from flask_restful import Api
from city import City
app=Flask(__name__)
app.secret_key='nihal'
api = Api(app)

api.add_resource(City,'/city')
app.run()