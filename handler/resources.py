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
        return jsonify(result_list)

    def getResourceById(self,rid):
        dao = ResourcesDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = Resource().build_dict_from_row(row)
            return jsonify(resource)



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
            return jsonify(result_list)


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
        return jsonify(result_list)

    def insertResource(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            rname = form['rname']
            catid = form['catId']
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
    def count(self):
        dao = ResourcesDAO()
        result = dao.count()
        return jsonify(count=result[0])
