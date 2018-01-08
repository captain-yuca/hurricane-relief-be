from flask import Blueprint, render_template, abort, jsonify, request
from handler.suppliers import SuppliersHandler

suppliers_route = Blueprint('suppliers_route', __name__)

@suppliers_route.route('/api/suppliers', methods=['GET','POST'])
def getAllSuppliers():
    """ Gets all suppliers """
    if request.method == 'GET':
            if not request.args:
                return SuppliersHandler().getAllSuppliers()
            else:
                return SuppliersHandler().searchSuppliers(request.args)
    elif request.method == 'POST':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405


@suppliers_route.route('/api/suppliers/<int:sid>', methods=['GET','POST','DELETE','PUT'])
def getSupplierById(sid):
    """ Gets a supplier by supplier id. """
    if request.method == 'GET':
        return SuppliersHandler().getSupplierById(sid)
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'PUT':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405


@suppliers_route.route('/api/suppliers/<int:sid>/stocks', methods=['GET','POST'])
def getStocksBySid(sid):
    """ Get all stocks pertaining to a given supplier. """
    if  request.method == 'GET':
        if not request.args:
            return SuppliersHandler().getStocksBySupplierId(sid)
        else:
            pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405

@suppliers_route.route('/api/suppliers/<int:sid>/transactions', methods=['GET', 'POST'])
def getTransactionsBySid(sid):
    """ Get all transactions pertaining to a given supplier. """
    if request.method == 'GET':
        if not request.args:
            return SuppliersHandler().getTransactionsBySupplierId(sid)
        else:
            pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405
