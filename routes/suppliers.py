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
        return SuppliersHandler().insert(request.get_json())
    else:
        return jsonify(Error="Method not allowed. "), 405


@suppliers_route.route('/api/suppliers/<int:sid>', methods=['GET','POST','DELETE','PUT'])
def getSupplierById(sid):
    """ Gets a supplier by supplier id. """
    if request.method == 'GET':
        return SuppliersHandler().getSupplierById(sid)
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

@suppliers_route.route('/api/suppliers/<int:sid>/transactions/<int:tid>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getSupplierTransactionById(sid, tid):
    """ Get all transactions pertaining to a given supplier. """
    if request.method == 'GET':
        if not request.args:
            return SuppliersHandler().getSupplierTransactionById(sid, tid)
        else:
            pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405

@suppliers_route.route('/api/suppliers/<int:sid>/address', methods=['GET', 'POST'])
def getAddressBySid(sid):
    if request.method == 'GET':
        if not request.args:
            return SuppliersHandler().getAddressBySid(sid)
        else:
            pass
    elif request.method == 'POST':
        pass
    else:
        return jsonify(Error="Method not allowed. "), 405

@suppliers_route.route('/api/suppliers/countPerRegion', methods=['GET', 'POST'])
def getSuppliersCountPerRegion():
    if request.method == 'GET':
        return SuppliersHandler().getSuppliersCountPerRegion()
    else:
        pass

@suppliers_route.route('/api/suppliers/<int:sid>/announcements', methods=['GET', 'POST'])
def getAnnouncementsBySid(sid):
    if request.method == 'GET':
        if not request.args:
            return SuppliersHandler().getAvailabilityAnnouncementsBySID(sid)
        else:
            pass
    elif request.method == 'POST':
        return SuppliersHandler().insertAvailabilityAnnouncementbySID(request.get_json(), sid)
    else:
        return jsonify(Error="Method not allowed. "), 405
@suppliers_route.route('/api/suppliers/<int:sid>/announcements/<int:ann_id>', methods=['GET', 'POST'])
def getAnnouncementDetailsByAnn_Id(sid,ann_id): #addedby H Jan 25 7 24 PM
    if request.method == 'GET':
        if not request.args:
            return SuppliersHandler.getAvailabilityAnnouncementsBySID(sid)
        else:
            pass
    elif request.method == 'POST':
        return SuppliersHandler().insertAvailabilityAnnouncementDetailByAnn_Id(request.get_json(), ann_id)
    else:
        return jsonify(Error="Method not allowed. "), 405 