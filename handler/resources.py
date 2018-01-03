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
        return jsonify(Resources=result_list)

    def getResourceById(self,rid):
        dao = ResourcesDAO()
        row = dao.getResourceById(rid)
        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = Resource().build_dict_from_row(row)
            return jsonify(Resource = resource)

    def searchResources(self, args):
        rname = args.get("rname")
        catId = args.get("catId")
        dao = ResourcesDAO()
        resources_list = []
        if(len(args)==2) and rname and catId:
            resources_list = dao.getResourcesByRnameAndCatId(rname, catId)
        elif(len(args)==1) and rname:
            resources_list = dao.getResourcesByRname(rname)
        elif(len(args)==1) and catId:
            resources_list = dao.getResourcesByCatId(catId)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in resources_list:
            result = Resource().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

