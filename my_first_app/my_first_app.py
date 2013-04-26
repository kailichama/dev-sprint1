# This is whre you can start you python file for your week1 web app
# Name: Kelly Chiang

import flask, flask.views
app = flask.Flask(__name__)

class View(flask.views.MethodView):
	def get(self):   
		return flask.render_template('index.html')

	def post(self):
		return "Works!"

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()