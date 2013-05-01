# This is whre you can start you python file for your week1 web app
# Name: Kelly Chiang

import flask, flask.views
app = flask.Flask(__name__)

class View(flask.views.MethodView):
	def get(self):   
		return flask.render_template('index.html') #flask defaults to a "templates" folder, remember to create a templates folder!

	def post(self): #when you have a get, should following with post if you want something to be displayed
		result = eval(flask.request.form['expression']) #links to the HTML form where the user types into the textbox named "expression"
		flask.flash(result)
		return self.get()

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST']) #lets the app know youre using more views, methods is a list

app.debug = True
app.run()

