from flask import Blueprint, render_template, abort, request
from handler.stocks import StocksHandler

stocks_route = Blueprint('stocks_route', __name__)

@stocks_route.route('/api/stocks', methods=['GET'])
def getAllStocks():
    if request.method == 'GET':
        if not request.args:
            return StocksHandler().getAllStocks()
        elif request.args.get('inStock')== 'true':
            return StocksHandler().getStocksInStock()
        elif request.args.get('inStock')== 'false':
            return StocksHandler().getStocksEmptyStock()
        else:
            return StocksHandler().searchStocks(request.args)
    else:
        return jsonify(Error="Method not allowed. "), 405


@stocks_route.route('/api/stocks/<int:rid>,<int:sid>', methods=['GET'])
def getStockById(rid, sid):
    if request.method == 'GET':
        return StocksHandler().getStockById(rid, sid)
    else:
        return jsonify(Error="Method not allowed. "), 405

@stocks_route.route('/api/stocks/qtysum', methods=['GET'])
def getSumOfResources():
    if request.method == 'GET':
        return StocksHandler().getSumOfResources()
    else:
        return jsonify(Error="Method not allowed. "), 405

#@stocks_route.route('/api/stocks/instock', methods=['GET', 'POST'])
#def getStocksInStock():
#    if request.method =='GET':
#        return StocksHandler().getStocksInStock()
