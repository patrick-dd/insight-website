#!/usr/bin/python																       
from flask import render_template, request, Flask
import pymysql as mdb
from a_model import ModelIt

app = Flask(__name__,static_url_path='/static')
if __name__=="__main__":
	app.run(host='0.0.0.0', port=5000)

@app.route('/')
@app.route('/input')
def cities_input():
	return render_template("input_0.html")

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/output')
def cities_output():
	#pull 'ID' from input field and store it
	city = request.args.get('ID')
	db = mdb.connect(
	    user='root', host='localhost', db = 'world',
	    charset ='utf8')
	with db:
		cur = db.cursor()
		#just select the city from the world_innodb that the user inputs
		cur.execute("SELECT Name, CountryCode,  Population FROM City WHERE Name='%s';" % city)
		query_results = cur.fetchall()
	cities = []
	for result in query_results:
		cities.append(dict(name=result[0], country=result[1], population=result[2]))
	#call a function from a_Model package. note we are only pulling one result in the query
	pop_input = cities[0]['population']
	the_result = ModelIt(city, pop_input)
	return render_template("output.html", cities = cities, the_result = the_result)

