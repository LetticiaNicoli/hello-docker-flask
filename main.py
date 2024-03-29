from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello World!'

def results():
  return {'fullfillmentText': 'This is a response from webhook'}

@app.route('/webhook', methods=['GET','POST'])
def webhook():
  return make_response(jsonify(results()))
  
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0',port=5000)
