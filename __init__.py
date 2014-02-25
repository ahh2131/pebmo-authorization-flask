from flask import render_template
from flask import Flask
from flask import request
import requests

app = Flask(__name__)


@app.route('/test2')
def hello_world():
	return render_template('index.html')


@app.route('/', methods = ['GET'])
def send_token():
    code = request.args.get('code')
    data = {
        "client_id":"1615",
        "client_secret":"SXHt7emkMzT36wmdLs96sgasMCqw5TAT",
        "code":code
        }
    url = "https://api.venmo.com/v1/oauth/access_token"
    response = requests.post(url, data)
    response_dict = response.json()
    return render_template('index.html', access_token=response_dict['access_token'])

if __name__ == '__main__':
    app.run(debug=True)
