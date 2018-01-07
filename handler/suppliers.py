from flask import jsonify
from dao.users import UsersDAO
from dao.suppliers import SuppliersDAO
from dao.stocks import StocksDAO

from models.supplier import Supplier
from models.stock import Stock

class SuppliersHandler:

    def getAllSuppliers(self):
        dao = SuppliersDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list=[]
        for row in suppliers_list:
            supplier = Supplier().build_dict_from_row(row)
            result_list.append(supplier)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, sid):
        dao = SuppliersDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            supplier = Supplier().build_dict_from_row(row)
            return jsonify(Supplier = supplier)

    def getStocksBySupplierId(self, sid):
        supplierDAO = SuppliersDAO()
        row = supplierDAO.getSupplierById(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            dao = StocksDAO()
            stocks_list = dao.getStocksBySid(sid)
            result_list=[]
            for row in stocks_list:
                stock = Stock().build_dict_from_row_resource(row)
                result_list.append(stock)
            return jsonify(stocks = result_list)


    def searchSuppliers(self, args):

        # Resource, Category and Stock parameters for searching
        allowed_keys={"rid", "rname", "catid", "catname", "qtysum", "currentpriceperitem"}

        # Add the min and max keys
        max_and_min_keys=set()
        for key in allowed_keys:
            max_and_min_keys.add("max-" + key)
            max_and_min_keys.add("min-" + key)
        allowed_keys = allowed_keys.union(max_and_min_keys)

        # Divide the args into min, max and equal parameters for query
        max_args={}
        min_args={}
        equal_args={}
        for key in args.keys():
            if key in allowed_keys and key[0:4] == "max-":
                max_args[key[4:]] = args[key]
            elif key in allowed_keys and key[0:4] == "min-":
                max_args[key[4:]] = args[key]
            elif key not in allowed_keys:
                return jsonify(Error="Malfromed query string"), 400
            else:
                equal_args[key] = args[key]

        dao = SuppliersDAO()
        suppliers_list= dao.getSuppliersByResourceParams(equal_args, max_args, min_args)
        result_list =[]
        for row in suppliers_list:
            supplier = Supplier().build_dict_from_row_stock(row)
            result_list.append(supplier)
        return jsonify(Suppliers=result_list)
