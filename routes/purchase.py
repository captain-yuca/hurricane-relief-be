from flask import Blueprint, render_template, abort
from flask import Flask, jsonify, request
from handler.purchase import PurchaseHandler

purchase_route = Blueprint('purchase_route', __name__)

@purchase_route.route('/api/purchases', methods=['GET', 'POST'])
def getAllPurchases():
    if not request.args:
        return PurchaseHandler().getAllPurchases()
    elif request.args.get('isReserved') == 'true':
        return PurchaseHandler().getAllReserves()
    elif request.args.get('isReserved') == 'false':
        return PurchaseHandler().getAllPaidPurchases()
    else:
        return PurchaseHandler().searchPurchases(request.args)

@purchase_route.route('/api/purchases/<int:purchase_id>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getPurchasesById(purchase_id):
    if request.method == 'GET':
        return PurchaseHandler().getPurchaseById(purchase_id)
