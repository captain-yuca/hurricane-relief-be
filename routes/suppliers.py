from flask import Blueprint, render_template, abort
from handler.suppliers import SuppliersHandler

suppliers_route = Blueprint('suppliers_route', __name__)

@suppliers_route.route('/api/suppliers', methods=['GET','POST'])
def getAllSuppliers():
    return SuppliersHandler().getAllSuppliers()

@suppliers_route.route('/api/suppliers/<int:sid>', methods=['GET','POST','DELETE','UPDATE'])
def getSupplierById(sid):
    if request.method == 'GET':
        return SuppliersHandler().getSupplierById(sid)
