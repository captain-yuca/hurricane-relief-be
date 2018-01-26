from flask import Blueprint, render_template, abort
from flask import Flask, jsonify, request
from handler.purchase import PurchaseHandler

purchase_route = Blueprint('purchase_route', __name__)

@purchase_route.route('/api/purchases', methods=['GET'])
def getAllPurchases():
    if request.method == 'GET':
        if not request.args:
            return PurchaseHandler().getAllPurchases()
        elif request.args.get('isReserved') == 'true':
            return PurchaseHandler().getAllReserves()
        elif request.args.get('isReserved') == 'false':
            return PurchaseHandler().getAllPaidPurchases()
        else:
            return PurchaseHandler().searchPurchases(request.args)
    else:
        return jsonify(Error="Method not allowed. "), 405


@purchase_route.route('/api/purchases/<int:purchase_id>', methods=['GET'])
def getPurchasesById(purchase_id):
    if request.method == 'GET':
        return PurchaseHandler().getPurchaseById(purchase_id)
    else:
        return jsonify(Error="Method not allowed. "), 405
