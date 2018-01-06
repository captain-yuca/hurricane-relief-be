from flask import Blueprint, render_template, abort, request
from handler.resourceTransactions import ResourceTransactionsHandler

resource_transactions_route = Blueprint('resource_transactions_route', __name__)

@resource_transactions_route.route('/api/transactions', methods=['GET', 'POST'])
def getAllTransactions():
    if not request.args:
        return ResourceTransactionsHandler().getAllTransactions()
    else:
        return ResourceTransactionsHandler().searchTransactions(request.args)

@resource_transactions_route.route('/api/transactions/<int:tid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getTransactionById(tid):
    if request.method == 'GET':
        return ResourceTransactionsHandler().getTransactionById(tid)
