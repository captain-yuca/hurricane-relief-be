from flask import jsonify
from dao.stocks import StocksDAO
from models.stock import Stock

class StocksHandler:

    def getAllStocks(self):
        dao = StocksDAO()
        stocks_list = dao.getAllStocks()
        result_list = []
        for row in stocks_list:
            result = Stock().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Stocks=result_list)

    def getStockById(self, rid, sid):
        dao = StocksDAO()
        row = dao.getStockById(rid, sid)
        if not row:
            return jsonify(Error="Stock Not Found"), 404
        else:
            stock = Stock().build_dict_from_row(row)
            return jsonify(Stock=stock)

    def searchStocks(self, args):
        rid = args.get("rid")
        sid = args.get("sid")
        qtysum = args.get("qtysum")
        currentpriceperitem = args.get("currentpriceperitem")
        resource = args.get("resource") #added for herbert stock mod
        user = args.get("user") #added for herbert stock mod
        dao = StocksDAO()
        stocks_list = []
        if(len(args) == 3) and rid and qtysum and currentpriceperitem:
            stocks_list = dao.getStocksByRidQtysumAndCurrentpriceperitem(rid, qtysum, currentpriceperitem)
        elif(len(args) == 3) and sid and qtysum and currentpriceperitem:
            stocks_list = dao.getStocksBySidQtysumAndCurrentpriceperitem(sid, qtysum, currentpriceperitem)
        elif(len(args) == 2) and rid and qtysum:
            stocks_list = dao.getStocksByRidAndQtysum(rid, qtysum)
        elif(len(args) == 2) and rid and currentpriceperitem:
            stocks_list = dao.getStocksByRidAndCurrentpriceperitem(rid, currentpriceperitem)
        elif(len(args) == 2) and sid and qtysum:
            stocks_list = dao.getStocksBySidAndQtysum(sid, qtysum)
        elif(len(args) == 2) and sid and currentpriceperitem:
            stocks_list = dao.getStocksBySidAndCurrentpriceperitem(sid, currentpriceperitem)
        elif(len(args) == 2) and qtysum and currentpriceperitem:
            stocks_list = dao.getStocksByQtysumAndCurrentpriceperitem(qtysum, currentpriceperitem)
        #added for herbert stock mod
        elif(len(args) == 2) and resource and user:
            stocks_list = dao.getStockByResourceAndUser(resource, user)
        #end of herbert added modifications. need to test.
        elif(len(args) == 1) and rid:
            stocks_list = dao.getStocksByRid(rid)
        elif(len(args) == 1) and sid:
            stocks_list = dao.getStocksBySid(sid)
        elif(len(args) == 1) and qtysum:
            stocks_list = dao.getStocksByQtySum(qtysum)
        elif(len(args) == 1) and currentpriceperitem:
            stocks_list = dao.getStocksByCurrentpriceperitem(currentpriceperitem)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in stocks_list:
            result = Stock().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Stocks=result_list)