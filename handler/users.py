from flask import jsonify
from dao.users import UsersDAO
from models.user import User

class UsersHandler:

    def getAllUsers(self):
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list=[]
        for row in users_list:
            user = User().build_dict_from_row(row)
            result_list.append(user)
        return jsonify(Users=result_list)
