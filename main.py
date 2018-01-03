from flask import Flask, jsonify, request
from handler.users import UsersHandler
from handler.addresses import AddressesHandler



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

# ADDRESSES
@app.route('/api/addresses', methods=['GET','POST'])
def getAllAddresses():
    return AddressesHandler().getAllAddresses()

@app.route('/api/addresses/<int:add_id>', methods=['GET','POST','DELETE','UPDATE'])
def getAddressById(add_id):
    if request.method == 'GET':
        return AddressesHandler().getAddressById(add_id)


if __name__ == '__main__':
    app.run()
