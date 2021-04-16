import json
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<pairname>')
def pair_signals(pairname):
	return 'This is {} buying signals'.format(pairname)


@app.route('/webhook', methods=['POST'])
def webhook():
	#print(request.data)
	data = json.loads(request.data)

	print(data['phoneNumbers'])

	return {
		"code" : "success",
	#	"message" : data

	}

if __name__ == '__main__':
	app.run(debug=True)
	