from flask import Flask, jsonify, request
from handler.users import UsersHandler



app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'

@app.route('/api/', methods=['GET'])
def getAllParts():
    return '<h3>HELLO</h3>'

# USERS
@app.route('/api/users', methods=['GET','POST'])
def getAllUsers():
    return UsersHandler().getAllUsers()

@app.route('/api/users/<int:uid>', methods=['GET','POST','DELETE','UPDATE'])
def getUserById(uid):
    if request.method == 'GET':
        return UsersHandler().getUserById(uid)


if __name__ == '__main__':
    app.run()
