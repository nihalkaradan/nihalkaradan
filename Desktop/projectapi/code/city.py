from flask_restful import Resource
import sqlite3
class City(Resource):
	def get(self):
		connection=sqlite3.connect('data.db')
		cursor=connection.cursor()
		query="SELECT CITY2,SUM(PASSENGERSTOCITY2) FROM test GROUP BY CITY2"
		result=cursor.execute(query)
		#print (result.fetchall())
		z={}
		for k,v in result.fetchall():
			z[k]=v
			
		return z
		
		connection.close()
		
			
		
			
