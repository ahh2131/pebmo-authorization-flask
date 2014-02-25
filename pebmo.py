from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/test2')
def hello_world():
	return render_template('index.html')


@app.route('/', methods = ['GET'])
def send_token():
    access_token = request.args.get('access_token')
    return render_template('index.html', access_token=access_token)

if __name__ == '__main__':
    app.run(debug=True)