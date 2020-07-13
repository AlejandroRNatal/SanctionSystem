from flask import Flask, request, jsonify

app = Flask(__name__)

# app.config["DEBUG"] = True

def test_data():
    data = [{'name':'',
              'sanctioned':True},]
    return data

@app.route('/', methods=['GET'])
def home():
    return "<h1>Sanctions Archive</h1><p>This site is a prototype API for verifying sanctioned indivs.</p>"

@app.route('/sanctioned/all',methods=['GET'])
def all_sanctioned():
    return jsonify(test_data())

if __name__ == "__main__":
    app.run(debug=True)