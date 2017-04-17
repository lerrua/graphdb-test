from flask_restful import Resource

from graphdb_test.models import User


class UserView(Resource):

    def get(self, user_id):
        """ Get user by id and a list of ids of 2nd/3rd degree connections """
        return User(id=int(user_id)).get()
