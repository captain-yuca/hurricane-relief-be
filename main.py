from flask import Flask, jsonify, request
from routes.users import users_route
from routes.requesters import requesters_route
from handler.suppliers import SuppliersHandler
from handler.resourceTransactionDetails import ResourceTransactionDetailsHandler

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
app.register_blueprint(users_route)

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

#RESOURCE TRANSACTION DETAILS
@app.route('/api/transactiondetails', methods=['GET', 'POST'])
def getAllTransactionDetails():
    if not request.args:
        return ResourceTransactionDetailsHandler().getAllTransactionDetails()
    else:
        return ResourceTransactionDetailsHandler().searchTransactionDetails(request.args)

@app.route('/api/transactiondetails/<int:tid>,<int:rid>', methods=['GET', 'POST'])
def getTransactionDetailsById(tid, rid):
    if request.method == 'GET':
        return ResourceTransactionDetailsHandler().getTransactionDetailsById(rid, tid)


    if request.method == 'GET':
        return SuppliersHandler().getSupplierById(sid)

# REQUESTER
app.register_blueprint(requesters_route)


if __name__ == '__main__':
    app.run()
