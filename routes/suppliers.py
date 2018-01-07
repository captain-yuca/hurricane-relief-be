from flask import Blueprint, render_template, abort, jsonify, request
from handler.suppliers import SuppliersHandler

suppliers_route = Blueprint('suppliers_route', __name__)

@suppliers_route.route('/api/suppliers', methods=['GET','POST'])
def getAllSuppliers():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        if not request.args:
            return SuppliersHandler().getAllSuppliers()
        else:
            return SuppliersHandler().searchSuppliers(request.args)
    else:
        return jsonify(Error="Method not allowed. "), 405

@suppliers_route.route('/api/suppliers/<int:sid>', methods=['GET','POST','DELETE','UPDATE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SuppliersHandler().getSupplierById(sid)
