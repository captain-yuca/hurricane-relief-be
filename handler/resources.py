from flask import jsonify
from dao.resources import ResourcesDAO
from models.resource import Resource

class ResourcesHandler:

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = Resource().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(resources=result_list)

    def getResourceById(self,rid):
        dao = ResourcesDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = Resource().build_dict_from_row(row)
            return jsonify(resource = resource)



    def searchResources(self, args):

        if args.get('category'):
            dao = ResourcesDAO()
            resources_list = dao.getResourcesByCategory(args.get('category'))
            result_list =[]
            for row in resources_list:
                resource = Resource().build_dict_from_row(row)
                result_list.append(resource)
            return jsonify(resources=result_list)
        elif args.get('requester'):
            dao = ResourcesDAO()
            resources_list = dao.getResourcesByRequester(args.get('requester'))
            result_list =[]
            for row in resources_list:
                resource = Resource().build_dict_from_row(row)
                result_list.append(resource)
            return jsonify(resources=result_list)
        elif args.get('supplier'):
            dao = ResourcesDAO()
            resources_list = dao.getResourcesBySupplier(args.get('supplier'))
            result_list =[]
            for row in resources_list:
                resource = Resource().build_dict_from_row(row)
                result_list.append(resource)
            return jsonify(resources=result_list)


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
        dao = ResourcesDAO()
        resources_list= dao.getResourcesByStockParams(equal_args, max_args, min_args)
        result_list =[]
        for row in resources_list:
            resource = Resource().build_dict_from_row(row)
            result_list.append(resource)
        return jsonify(resources=result_list)

    #     rname = args.get("rname")
    #     catId = args.get("catId")
    #     supplier = args.get("supplier") #added by Herbert to implement 14
    #     req_id = args.get("req_id") #-H
    #     nid = args.get("nid") #-H
    #     requester = args.get("requester") #-H
    #     category = args.get("category") #-H
    #     dao = ResourcesDAO()
    #     resources_list = []
    #     if(len(args)==2) and rname and catId:
    #         resources_list = dao.getResourcesByRnameAndCatId(rname, catId)
    #     elif(len(args)==1) and rname:
    #         resources_list = dao.getResourcesByRname(rname)
    #     elif(len(args)==1) and catId:
    #         resources_list = dao.getResourcesByCatId(catId)
    #     elif(len(args) == 1) and supplier: #added by Herbert to implement 14
    #         resources_list = dao.getResourcesBySupplier(supplier)
    #     elif(len(args) == 1) and req_id: # added by Herbert
    #         resources_list = dao.getResourcesByRequest(req_id)
    #     elif (len(args) == 1) and nid:  # added by Herbert
    #         resources_list = dao.getResourcesByNID(nid)
    #     elif (len(args) == 1) and requester:  # added by Herbert (requester is a username)
    #         resources_list = dao.getResourcesByRequester(requester)
    #     elif (len(args) == 1) and category:  # added by Herbert
    #         resources_list = dao.getResourcesByCategory
    #     else:
    #         return jsonify(Error = "Malformed query string"), 400
    #     result_list = []
    #     for row in resources_list:
    #         result = Resource().build_dict_from_row(row)
    #         result_list.append(result)
    #     return jsonify(Resources=result_list)
    def insertResource(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            rname = form['rname']
            catid = form['catid']
            if rname and catid:
                dao = ResourcesDAO()
                rid = dao.insert(rname, catid)
                result = Resource().build_dict_from_row(dao.getResourceById(rid))
                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Unepected attributes in post request"), 400

    def updateResource(self, rid, form):
        dao = ResourcesDAO()
        if not dao.getResourceById(rid):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                rname = form['rname']
                catid = form['catid']
                if rname and catid:
                    rid = dao.update(rid, rname, catid)
                    result = Resource().build_dict_from_row(dao.getResourceById(rid))
                    return jsonify(result), 201
                else:
                    return jsonify(Error="Unexpected attributes in put request"), 400