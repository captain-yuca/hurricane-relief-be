from flask import Flask, jsonify, request
from handler.users import UsersHandler
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
    

if __name__ == '__main__':
    app.run()
