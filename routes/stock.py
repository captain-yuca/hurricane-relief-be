from flask import Blueprint, render_template, abort, request
from handler.stocks import StocksHandler

stocks_route = Blueprint('stocks_route', __name__)

@stocks_route.route('/api/stocks', methods=['GET', 'POST'])
def getAllStocks():
    if not request.args:
        return StocksHandler().getAllStocks()
    elif request.args.get('inStock')== 'true':
        return StocksHandler().getStocksInStock()
    elif request.args.get('inStock')== 'false':
        return StocksHandler().getStocksEmptyStock()
    else:
        return StocksHandler().searchStocks(request.args)

@stocks_route.route('/api/stocks/<int:rid>,<int:sid>', methods=['GET', 'POST', 'DELETE', 'UPDATE'])
def getStockById(rid, sid):
    if request.method == 'GET':
        return StocksHandler().getStockById(rid, sid)

@stocks_route.route('/api/stocks/qtysum', methods=['GET', 'POST'])
def getSumOfResources():
    if request.method == 'GET':
        return StocksHandler().getSumOfResources()
    else:
        pass
#@stocks_route.route('/api/stocks/instock', methods=['GET', 'POST'])
#def getStocksInStock():
#    if request.method =='GET':
#        return StocksHandler().getStocksInStock()
