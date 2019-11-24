from flask import Flask, request, jsonify, redirect, abort, json
from flask_cors import CORS
from testjson import jsonstring
import constants
import time

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.errorhandler(404)
def page_not_found(e):
	print("errorhandler called")
	# kall()
	response = jsonify('lmao')
	response.status_code = 404
	return response


@app.route('/login', methods=['POST', 'OPTIONS'])
def loginFunction():

	if (request.method == "POST"):
		print("post method used")
		# data = dict(request.get_data().decode('utf-8'))
		print("the request is ", request.get_data().decode('utf-8'))

		email = request.json['email']
		password = request.json['password']

		if (email == "test@test.com" and password == "test"):
			print("user successfully logged in")
			respose_data = {'fullName': "test boy", "email": "test@test.com"}
			return jsonify(respose_data)
		else:
			print("not logged in successfully")
			abort(404)
			return redirect('/404')
	# password = data['password']

	# print("email ", email, "password", password)
		print('json', request.json['email'])

	return jsonify("Test")


@app.route('/frameworkContents/')
def module():
	if request.args:
		frameworkId = int(request.args['frameworkId'])
		if (frameworkId == constants.FLASK):
			from flaskjson import flaskjsonstring
			return jsonify(flaskjsonstring)
		if (frameworkId == constants.NODE):
			from nodejson import nodejsonstring
			return jsonify(nodejsonstring)
		if (frameworkId == constants.EXPRESS):
			from expressjson import expressjsonstring
			return jsonify(expressjsonstring)
		if (frameworkId == constants.DJANGO):
			from djangojson import djangojsonstring
			return jsonify(djangojsonstring)
		if (frameworkId == constants.CPP):
			from cppjson import cppjsonstring
			return jsonify(cppjsonstring)

@app.route('/hassignedup/')
def testFunction():
	print("has hasSignedUp")
	print("request data", request.json)
	if (request.args):
		print(request.args)
		email = request.args['email']
		frameworkId = str(request.args['frameworkId'])
		print("EMAIL", email, frameworkId)
		if (email == "test@test.com" and frameworkId == 'flask'):
			print("found framework")
			return jsonify("damn")
		else:
			abort(404)
			return redirect ('/404')
	else:
		return jsonify("loool")

@app.route('/password_text_editor/')
def text_pass():
	print("textEditor password")
	print("request data", request.args)
	if (request.args):
		print(request.args)
		email = request.args['email']
		frameworkId = str(request.args['frameworkId'])
		print("EMAIL", email, frameworkId)
		return jsonify('password')
	else:
		return jsonify("loool")


@app.route('/frameworkdetails', methods=['GET'])
def details():
	print('frameworkdetails')
	print("frameworkdetails")
	return jsonify(jsonstring)

init = False
@app.route('/initialize', methods=['POST'])
def fr_init():
	print('frinit')
	print("request data", request.json)
	data = request.json
	global init
	if (data):
		print('request args')
		email = data['email']
		frameworkName = data['frameworkName']
		print("init called")
		time.sleep(4)
		if (not init):
			init = True
			abort(404)
			return redirect('/404')
		else:
			return jsonify('test')
	else:
		abort(404)
		return ('/404')

text_editor_init = False
@app.route('/start-text-editor', methods=['GET', 'PUT', 'DELETE'])
def text_init():
	if request.method == 'DELETE':
		return jsonify('lolcat')
	global text_editor_init
	time.sleep(2)
	if (not text_editor_init):
		text_editor_init = True
		abort(404)
		return jsonify('/404')
	else:
		text_editor_init = False
		return jsonify("http://google.co.in")

deploy_server_init = False
@app.route('/deploy_server', methods=['GET', 'PUT', 'DELETE'])
def deploy_init():
	if request.method == 'DELETE':
		return jsonify('lolcat')
	global deploy_server_init
	time.sleep(2)
	if (not deploy_server_init):
		deploy_server_init = True
		abort(404)
		return jsonify('/404')
	else:
		deploy_server_init = False
		return jsonify("http://google.co.in")

if __name__ == "__main__":
    app.run(debug=True)
