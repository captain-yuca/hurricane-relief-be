from flask import jsonify
from dao.users import UsersDAO
from dao.suppliers import SuppliersDAO
from dao.stocks import StocksDAO
from dao.resourceTransactions import ResourceTransactionsDAO
from dao.resourceTransactionDetails import ResourceTransactionDetailsDAO
from dao.addresses import AddressesDAO
from dao.resources import ResourcesDAO #added by Herbert Jan 23 for a post
from dao.availability_announcements import AvailabilityAnnouncementsDAO #added by Herbert
from dao.availabilityAnnoucementDetails import AvailabilityAnnoucementDetailsDAO #H again
from dao.categories import CategoriesDAO

from models.supplier import Supplier
from models.stock import Stock
from models.resourceTransaction import ResourceTransaction
from models.resourceTransactionDetails import ResourceTransactionDetails
from models.address import Address
from models.availability_announcement import AvailabilityAnnouncement


class SuppliersHandler:

    def getAllSuppliers(self):
        dao = SuppliersDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list=[]
        for row in suppliers_list:
            supplier = Supplier().build_dict_from_row(row)
            result_list.append(supplier)
        return jsonify(result_list)

    def getSupplierById(self, sid):
        dao = SuppliersDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404
        else:
            supplier = Supplier().build_dict_from_row(row)
            return jsonify(supplier)

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
            return jsonify(result_list)

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
            return jsonify(result_list)

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
        result = ResourceTransaction().build_dict_from_table_no_sup_no_pur(transaction)
        return jsonify(result)



    def searchSuppliers(self, args):

        # Query parameters allowed when searching
        # These parameters are from Resource, Category and Stock
        allowed_keys={"rid", "rname", "catid", "catname",  "region", "city"}
        allowed_range_keys={"qtysum", "currentpriceperitem","zipcode"}
        # Allow every query parameter stated in allowed_keys to have a min or max value
        max_and_min_keys=set()
        for key in allowed_range_keys:
            max_and_min_keys.add("max-" + key)
            max_and_min_keys.add("min-" + key)
        allowed_keys = allowed_keys.union(max_and_min_keys)
        allowed_keys = allowed_keys.union(allowed_range_keys)

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
        return jsonify(result_list)

    def searchStocks(self, sid, args):
        dao = SuppliersDAO()
        row = dao.getSupplierById(sid)
        if not row:
            return jsonify(Error = "Supplier Not Found"), 404

        allowed_keys={"rid", "rname", "catid", "catname"}
        allowed_range_keys={"qtysum", "currentpriceperitem"}

        # Allow every query parameter stated in allowed_keys to have a min or max value
        max_and_min_keys=set()
        for key in allowed_range_keys:
            max_and_min_keys.add("max-" + key)
            max_and_min_keys.add("min-" + key)
        allowed_keys = allowed_keys.union(max_and_min_keys)
        allowed_keys = allowed_keys.union(allowed_range_keys)


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

        # Added sid for searching specific uid
        equal_args['sid'] = sid


        # Get all the results for the search
        dao = StocksDAO()
        stocks_list= dao.getStocksByParamsNoSupplier(equal_args, max_args, min_args)
        result_list =[]
        for row in stocks_list:
            stock = Stock().build_dict_from_row_no_supplier(row)
            result_list.append(stock)
        return jsonify(result_list)

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
            return jsonify(result_list)

    def getSuppliersCountPerRegion(self):
        dao = SuppliersDAO()
        counts_list = dao.getSuppliersCountPerRegion()
        result_list = []
        for row in counts_list:
            count = Address().build_dict_from_row_count(row)
            result_list.append(count)
        return jsonify(result_list)


    def insert(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            uid = form['uid']
            if uid:
                dao = UsersDAO()
                if not dao.getUserById(uid):
                    return jsonify(Error="User not found"), 404
                dao = SuppliersDAO()
                sid = dao.insert(uid)
                result = Supplier().build_dict_from_row(dao.getSupplierById(sid))
                return jsonify(result)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def count(self):
        dao = SuppliersDAO()
        result = dao.count()
        return jsonify(result[0])

#this one feel like a damn placeholder, so much shit to fix -Herbert. Mostly confused since its a lot of stuff being added
    def insertAvailabilityAnnouncementDetailByAnn_Id(self, form, ann_id):
        print(len(form))
        if len(form) == 3:
            rid = form['rid']
            qty = form['qty']
            priceattime = form['priceattime']
            sid=None
            # rm['date'] #DATE has yet to be added to documentation

            if rid and qty and priceattime:

                dao = ResourcesDAO()
                if not dao.getResourceById(rid):
                    return jsonify(Error="Resource not found"), 404

                dao = AvailabilityAnnouncementsDAO()
                announcement=dao.getAnnouncementById(ann_id)
                if not announcement:
                    return jsonify(Error="Announcement not found"),404
                else:
                    sid=announcement[1] #verify this is true -H

                dao = AvailabilityAnnoucementDetailsDAO()
                if not dao.getAnnouncementDetailsById(ann_id,rid):
                    dao.insertAvailabilityAnnouncementDetails(ann_id, rid, qty, priceattime)
                else:
                    return jsonify(Error="Duplicate Primary Key"), 400

                dao = StocksDAO()
                if not dao.getStockById(rid, sid):
                    # add to stock if doesnt exist
                    dao.insertStock(rid, sid, qty, priceattime)
                else:
                    astock = dao.getStockById(rid, sid)
                    newqty = astock[11] + qty
                    dao.updateStock(rid, sid, newqty, priceattime)


                dao = AvailabilityAnnouncementsDAO()
                table = dao.getAnnouncementByIdWithDetails(ann_id)
                if not table:
                    return jsonify(Error="Availability Announcement Not Found"), 404
                else:
                    result = AvailabilityAnnouncement().build_dict_from_table_details(table)
                    return jsonify(result)
        elif len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            rname = form['rname']
            catid = form['catid']
            qty = form['qty']
            priceattime = form['priceattime']
            rid = None
            sid = None
            if rname and catid and qty and priceattime:
                dao2 = CategoriesDAO()

                dao = ResourcesDAO()
                resource = dao.getResourcesByRname(rname)
                if not resource:
                    if not dao2.getCategoryById(catid):
                        return jsonify(Error="Category not found")
                    rid = dao.insert(rname, catid)
                else:
                    rid = (resource[0])[0]
                    print(rid)
                dao = AvailabilityAnnouncementsDAO()
                announcement = dao.getAnnouncementById(ann_id)
                if not announcement:
                    return jsonify(Error="Announcement not found"), 404
                else:
                    sid = announcement[1]  # verify this is true -H
                dao = AvailabilityAnnoucementDetailsDAO()
                if not dao.getAnnouncementDetailsById(ann_id, rid):
                    dao.insertAvailabilityAnnouncementDetails(ann_id, rid, qty, priceattime)
                else:
                    return jsonify(Error="Duplicate Primary Key"), 400
                dao = StocksDAO()
                if not dao.getStockById(rid, sid):
                    # add t
                    # o stock if doesnt exist
                    dao.insertStock(rid, sid, qty, priceattime)
                else:
                    astock = dao.getStockById(rid, sid)
                    newqty = astock[11] + qty
                    dao.updateStock(rid, sid, newqty, priceattime)
                    # increase number of items in stock by qty. of each damn item. shit.
                # dao = SuppliersDAO() # do I even need this one?
                # dao2 = AvailabilityAnnouncementsDAO()

                dao = AvailabilityAnnouncementsDAO()
                table = dao.getAnnouncementByIdWithDetails(ann_id)
                if not table:
                    return jsonify(Error="Availability Announcement Not Found"), 404
                else:
                    result = AvailabilityAnnouncement().build_dict_from_table_details(table)
                    return jsonify(result)

    def insertAvailabilityAnnouncementbySID(self, form, sid): #added by herbert for post announcements by supplier
        print(len(form))
        if len(form) == 3:
            rid = form['rid']
            qty = form['qty']
            priceattime = form['priceattime']
            #rm['date'] #DATE has yet to be added to documentation

            if rid and qty and priceattime:

                dao = ResourcesDAO()
                if not dao.getResourceById(rid):
                    return jsonify(Error="Resource not found"), 404

                dao = AvailabilityAnnouncementsDAO()
                ann_id = dao.insertAvailabilityAnnouncement(sid)

                dao = StocksDAO()
                if not dao.getStockById(rid, sid):
                    #add t
                    # o stock if doesnt exist
                    dao.insertStock(rid, sid, qty, priceattime)
                else:
                    astock = dao.getStockById(rid, sid)
                    newqty = astock[11]+qty
                    dao.updateStock(rid,sid, newqty, priceattime)
                    #increase number of items in stock by qty. of each damn item. shit.
                #dao = SuppliersDAO() # do I even need this one?
                #dao2 = AvailabilityAnnouncementsDAO()
                dao = AvailabilityAnnoucementDetailsDAO()
                dao.insertAvailabilityAnnouncementDetails(ann_id,rid, qty, priceattime) #do a loop to add all the fields
                dao = AvailabilityAnnouncementsDAO()
                table = dao.getAnnouncementByIdWithDetails(ann_id)
                if not table:
                    return jsonify(Error="Availability Announcement Not Found"), 404
                else:
                    result = AvailabilityAnnouncement().build_dict_from_table_details(table)
                    return jsonify(result)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
        elif len(form) !=4:
            return jsonify(Error="Malformed post request"), 400
        else:
            rname = form['rname']
            catid = form['catid']
            qty = form['qty']
            priceattime = form['priceattime']
            rid = None
            if rname and catid and qty and priceattime:
                dao2 = CategoriesDAO()
                dao = ResourcesDAO()
                resource = dao.getResourcesByRname(rname)
                if not resource:
                    if not dao2.getCategoryById(catid):
                        return jsonify(Error="Category not found")
                    rid=dao.insert(rname,catid)
                else:
                    rid=(resource[0])[0]
                    print(rid)
                dao = AvailabilityAnnouncementsDAO()
                ann_id = dao.insertAvailabilityAnnouncement(sid)

                dao = StocksDAO()
                if not dao.getStockById(rid, sid):
                    # add t
                    # o stock if doesnt exist
                    dao.insertStock(rid, sid, qty, priceattime)
                else:
                    astock = dao.getStockById(rid, sid)
                    newqty = astock[11] + qty
                    dao.updateStock(rid, sid, newqty, priceattime)
                    # increase number of items in stock by qty. of each damn item. shit.
                # dao = SuppliersDAO() # do I even need this one?
                # dao2 = AvailabilityAnnouncementsDAO()
                dao = AvailabilityAnnoucementDetailsDAO()
                dao.insertAvailabilityAnnouncementDetails(ann_id, rid, qty,
                                                          priceattime)  # do a loop to add all the fields
                dao = AvailabilityAnnouncementsDAO()
                table = dao.getAnnouncementByIdWithDetails(ann_id)
                if not table:
                    return jsonify(Error="Availability Announcement Not Found"), 404
                else:
                    result = AvailabilityAnnouncement().build_dict_from_table_details(table)
                    return jsonify(result)

            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
    def getAvailabilityAnnouncementsBySID(self, sid):
    #TOMORROW FIX: WHATS UP WITH THE DIC. SOMETHING ABOUT ADMIN.
        supplierDAO = SuppliersDAO()
        supplier = supplierDAO.getSupplierById(sid)
        if not supplier:
            return jsonify(Error="Supplier Not Found"), 404

        dao = AvailabilityAnnouncementsDAO()
        table = dao.getAnnouncementBySIDWithDetails(sid)
        if not table:
            return jsonify(Error="Availability Announcement Not Found"), 404
        else:
            result = AvailabilityAnnouncement().build_dict_from_table_no_sup(table)
            return jsonify(result)

    def getAvailabilityAnnouncementByIds(self, sid,ann_id):
        supplierDAO = SuppliersDAO()
        supplier = supplierDAO.getSupplierById(sid)
        if not supplier:
            return jsonify(Error="Supplier Not Found"), 404

        dao = AvailabilityAnnouncementsDAO()
        supplier = dao.getAnnouncementBySIDWithDetails(sid)
        if not supplier[0]:
            return jsonify(Error="Availability Announcement not found"), 404
        result=[]
        result.append(dao.getAnnouncementById(ann_id))
        if not result:
            return jsonify(Error="Availability Announcement Not Found"), 404
        else:
            newresult = AvailabilityAnnouncement().build_dict_from_table_no_sup(result)
            return jsonify(newresult)
