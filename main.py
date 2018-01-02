from flask import Flask, jsonify, request




app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'

@app.route('/api/', methods=['GET'])
def getAllParts():
    return '<h3>HELLO</h3>'


if __name__ == '__main__':
    app.run()
