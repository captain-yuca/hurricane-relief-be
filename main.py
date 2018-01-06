from flask import Flask, jsonify, request
from handler.users import UsersHandler
from handler.suppliers import SuppliersHandler
from handler.requesters import RequestersHandler
from handler.resources import ResourcesHandler
from handler.categories import CategoriesHandler
from handler.resourceTransactions import ResourceTransactionsHandler



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

# RESOURCES
@app.route('/api/resources', methods=['GET', 'POST'])
def getAllResources():
    if not request.args:
        return ResourcesHandler().getAllResources()
    else:
        return ResourcesHandler().searchResources(request.args)

@app.route('/api/resources/<int:rid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getResourceById(rid):
    if request.method == 'GET':
        return ResourcesHandler().getResourceById(rid)

# CATEGORIES
@app.route('/api/categories', methods=['GET', 'POST'])
def getAllCategories():
    if not request.args:
        return CategoriesHandler().getAllCategories()
    else:
        return CategoriesHandler().searchCategories(request.args)

@app.route('/api/categories/<int:catid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getCategoryById(catid):
    if request.method == 'GET':
        return CategoriesHandler().getCategoryById(catid)

#RESOURCE TRANSACTIONS
@app.route('/api/transactions', methods=['GET', 'POST'])
def getAllTransactions():
    if not request.args:
        return ResourceTransactionsHandler().getAllTransactions()
    else:
        return ResourceTransactionsHandler().searchTransactions(request.args)

@app.route('/api/transactions/<int:tid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getTransactionById(tid):
    if request.method == 'GET':
        return ResourceTransactionsHandler().getTransactionById(tid)

# SUPPLIER
@app.route('/api/suppliers', methods=['GET','POST'])
def getAllSuppliers():
    return SuppliersHandler().getAllSuppliers()

@app.route('/api/suppliers/<int:sid>', methods=['GET','POST','DELETE','UPDATE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SuppliersHandler().getSupplierById(sid)

# REQUESTER
@app.route('/api/requesters', methods=['GET','POST'])
def getAllRequesters():
    return RequestersHandler().getAllRequesters()

@app.route('/api/requesters/<int:nid>', methods=['GET','POST','DELETE','UPDATE'])
def getRequesterById(nid):
    if request.method == 'GET':
        return RequestersHandler().getRequesterById(nid)

if __name__ == '__main__':
    app.run()
