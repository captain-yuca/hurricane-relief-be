from flask import jsonify
from dao.users import UsersDAO
from dao.suppliers import SuppliersDAO
from dao.stocks import StocksDAO
from dao.resourceTransactions import ResourceTransactionsDAO
from dao.resourceTransactionDetails import ResourceTransactionDetailsDAO
from dao.addresses import AddressesDAO

from models.supplier import Supplier
from models.stock import Stock
from models.resourceTransaction import ResourceTransaction
from models.resourceTransactionDetails import ResourceTransactionDetails
from models.address import Address


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
        # Check if supplier exists
        supplierDAO = SuppliersDAO()
        row = supplierDAO.getSupplierById(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        #If supplier found, get all the stocks from that supplier
        else:
            dao = StocksDAO()
            stocks_list = dao.getStocksBySid(sid)
            result_list=[]
            for row in stocks_list:
                stock = Stock().build_dict_from_row_resource(row)
                result_list.append(stock)
            return jsonify(stocks = result_list)

    def getTransactionsBySupplierId(self, sid):
        supplierDAO = SuppliersDAO()
        row = supplierDAO.getSupplierById(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        #If supplier found, get all the stocks from that supplier
        else:
            dao = ResourceTransactionsDAO()
            transactions_list = dao.getTransactionsBySid(sid)
            result_list=[]
            for row in transactions_list:
                transaction = ResourceTransaction().build_dict_from_row(row)
                result_list.append(transaction)
            return jsonify(transactions = result_list)

    def getSupplierTransactionById(self, sid, tid):
        supplierDAO = SuppliersDAO()
        supplier = supplierDAO.getSupplierById(sid)
        if not supplier:
            return jsonify(Error = "Supplier Not Found"), 404
        #If supplier found, get all the stocks from that supplier
        transactionsDao = ResourceTransactionsDAO()
        transaction = transactionsDao.getTransactionById(tid)
        if not transaction:
            return jsonify(Error = "Transaction Not Found"), 404
        result = ResourceTransaction().build_dict_from_table(transaction)
        return jsonify(transaction = result)

    def getTransactionDetailsById(self, sid, tid):
        supplierDAO = SuppliersDAO()
        supplier = supplierDAO.getSupplierById(sid)
        if not supplier:
            return jsonify(Error = "Supplier Not Found"), 404
        #If supplier found, get all the stocks from that supplier
        transactionsDao = ResourceTransactionsDAO()
        transaction = transactionsDao.getTransactionById(tid)
        if not transaction or transaction[2]  != sid:
            return jsonify(Error = "Transaction Not Found"), 404

        detailsDAO = ResourceTransactionDetailsDAO()
        details_list =  detailsDAO.getTransactionDetailsByTid(tid)
        result_list = []
        for row in details_list:
            detail = ResourceTransactionDetails().build_dict_from_row_resource(row)
            result_list.append(detail)
        return jsonify(details=result_list)



    def searchSuppliers(self, args):

        # Query parameters allowed when searching
        # These parameters are from Resource, Category and Stock
        allowed_keys={"rid", "rname", "catid", "catname", "qtysum", "currentpriceperitem", "zipcode", "region", "city"}

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
        dao = SuppliersDAO()
        suppliers_list= dao.getSuppliersByResourceParams(equal_args, max_args, min_args)
        result_list =[]
        for row in suppliers_list:
            supplier = Supplier().build_dict_from_row_stock(row)
            result_list.append(supplier)
        return jsonify(Suppliers=result_list)

    def getAddressBySid(self, sid):
        supplierDAO = SuppliersDAO()
        row = supplierDAO.getSupplierById(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        # If supplier found, get all the stocks from that supplier
        else:
            dao = AddressesDAO()
            address = dao.getAddressBySid(sid)
            result_list = Address().build_dict_from_row(address)
            return jsonify(Address=result_list)

    def getSuppliersCountPerRegion(self):
        dao = SuppliersDAO()
        counts_list = dao.getSuppliersCountPerRegion()
        result_list = []
        for row in counts_list:
            count = Address().build_dict_from_row_count(row)
            result_list.append(count)
        return jsonify(suppliers_per_region=result_list)


