from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        print(request.args)
        data = "request"
    if(request.method == 'POST'):
        try:
            data = request.get_json()['query'] + "de-gozaru"
        except:
            data = ""
    print(data)
    return jsonify({'data': data})

if __name__ == '__main__':
  
    app.run(debug = True)