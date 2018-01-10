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

    def getStocksInStock(self):
        dao = StocksDAO()
        stocks_list = dao.getStocksInStock()
        result_list = []
        for row in stocks_list:
            result = Stock().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Stocks=result_list)

    def getSumOfResources(self):
        dao = StocksDAO()
        sum_list = dao.getSumOfResources()
        result_list = []
        for row in sum_list:
            result = Stock().build_dict_from_row_sum(row)
            result_list.append(result)
        return jsonify(Sums=result_list)


    def searchStocks(self, args):
        # Query parameters allowed when searching
        # These parameters are from Resource, Category and Stock
        allowed_keys={"rid", "rname", "catid", "qtysum", "currentpriceperitem", "zipcode", "region", "city"}

        # Allow every query parameter stated in allowed_keys to have a min or max value
        max_and_min_keys=set()
        for key in allowed_keys:
            max_and_min_keys.add("max-" + key)
            max_and_min_keys.add("min-" + key)
        allowed_keys = allowed_keys.union(max_and_min_keys)

        # Divide the args given by user into min, max and equal parameters for use in DAO
        max_args={}
        min_args={}
        equal_args={}
        for key in args.keys():
            if key in allowed_keys and key[0:4] == "max-":
                max_args[key[4:]] = args[key]
            elif key in allowed_keys and key[0:4] == "min-":
                min_args[key[4:]] = args[key]
            elif key not in allowed_keys:
                return jsonify(Error="Malfromed query string"), 400
            else:
                equal_args[key] = args[key]

        # Get all the results for the search
        dao = StocksDAO()
        resources_list= dao.getStocksByParams(equal_args, max_args, min_args)
        result_list =[]
        for row in resources_list:
            resource = Stock().build_dict_from_row(row)
            result_list.append(resource)
        return jsonify(stocks=result_list)
