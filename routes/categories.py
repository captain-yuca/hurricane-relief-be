from flask import Blueprint, render_template, abort, request
from handler.categories import CategoriesHandler

categories_route = Blueprint('categories_route', __name__)

@categories_route.route('/api/categories', methods=['GET', 'POST'])
def getAllCategories():
    if not request.args:
        return CategoriesHandler().getAllCategories()
    else:
        return CategoriesHandler().searchCategories(request.args)
