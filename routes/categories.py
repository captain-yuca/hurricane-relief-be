from flask import Blueprint, render_template, abort, request, jsonify
from handler.categories import CategoriesHandler

categories_route = Blueprint('categories_route', __name__)

@categories_route.route('/api/categories', methods=['GET', 'POST'])
def getAllCategories():
    if request.method == 'GET':
        if not request.args:
            return CategoriesHandler().getAllCategories()
        else:
            return CategoriesHandler().searchCategories(request.args)
    elif request.method == 'POST':
        return CategoriesHandler().insertCategory(request.get_json())
    else:
        return jsonify(Error="Method not allowed."), 405

@categories_route.route('/api/categories/<int:catid>', methods=['GET', 'PUT'])
def getCategoryById(catid):
    if request.method == 'GET':
        return CategoriesHandler().getCategoryById(catid)
    elif request.method == 'PUT':
        return CategoriesHandler().updateCategory(catid, request.get_json())
    else:
        return jsonify(Error="Method not allowed."), 405
