from flask import Flask, jsonify, request
from handler.users import UsersHandler
from handler.addresses import AddressesHandler
from handler.payment_info import PaymentInfoHandler



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

@app.route('/api/users/<int:uid>/addresses', methods=['GET','POST','DELETE','UPDATE'])
def getAddressesByUserId(uid):
    if request.method == 'GET':
        return UsersHandler().getAddressesByUserId(uid)

# ADDRESSES
@app.route('/api/addresses', methods=['GET','POST'])
def getAllAddresses():
    return AddressesHandler().getAllAddresses()

@app.route('/api/addresses/<int:add_id>', methods=['GET','POST','DELETE','UPDATE'])
def getAddressById(add_id):
    if request.method == 'GET':
        return AddressesHandler().getAddressById(add_id)

# PAYMENT_INFO
@app.route('/api/payment_info', methods=['GET','POST'])
def getAllPaymentInfo():
    return PaymentInfoHandler().getAllPaymentInfo()

@app.route('/api/payment_info/<int:pi_id>', methods=['GET','POST','DELETE','UPDATE'])
def getPaymentInfoById(pi_id):
    if request.method == 'GET':
        return PaymentInfoHandler().getPaymentInfoById(pi_id)

if __name__ == '__main__':
    app.run()
