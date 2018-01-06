from flask import Flask, jsonify, request
from routes.users import users_route
from routes.requesters import requesters_route
from routes.suppliers import suppliers_route
from routes.resources import resources_route
from routes.categories import categories_route
from routes.resource_transactions import resource_transactions_route
from routes.purchase import purchase_route
from handler.resourceTransactionDetails import ResourceTransactionDetailsHandler




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
app.register_blueprint(resources_route)

# CATEGORIES
app.register_blueprint(categories_route)

# RESOURCE transactions
app.register_blueprint(resource_transactions_route)

# SUPPLIER
app.register_blueprint(suppliers_route)

# REQUESTER
app.register_blueprint(requesters_route)

#PURCHASE
app.register_blueprint(purchase_route)


if __name__ == '__main__':
    app.run()
