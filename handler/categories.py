from flask import jsonify
from dao.categories import CategoriesDAO
from models.category import Category

class CategoriesHandler:

    def getAllCategories(self):
        dao = CategoriesDAO()
        categories_list = dao.getAllCategories()
        result_list = []
        for row in categories_list:
            result = Category().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Categories=result_list)

    def getCategoryById(self, catId):
        dao = CategoriesDAO()
        row = dao.getCategoryById(catId)
        if not row:
            return jsonify(Error = "Category Not Found"), 404
        else:
            category = Category().build_dict_from_row(row)
            return jsonify(Category = category)


    def searchCategories(self, args):
        catName = args.get("catName")
        dao = CategoriesDAO()
        categories_list = []
        if(len(args)==1 and catName):
            categories_list = dao.getCategoriesByName(catName)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in categories_list:
            result = Category().build_dict_from_row(row)
            result_list.append(result)
        return jsonify(Categories=result_list)

    def insertCategory(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            catname = form['catname']
            if catname:
                dao = CategoriesDAO()
                catid = dao.insert(catname)
                result = Category().build_dict_from_row(dao.getCategoryById(catid))
                return jsonify(Category=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateCategory(self, catid, form):
        dao = CategoriesDAO()
        if not dao.getCategoryById(catid):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                catname = form['catname']
                if catname:
                    catid = dao.update(catid, catname)
                    result = Category().build_dict_from_row(dao.getCategoryById(catid))
                    return jsonify(Category=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400