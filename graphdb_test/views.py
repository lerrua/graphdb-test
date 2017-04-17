from flask_restful import Resource

from graphdb_test.models import User


class UserView(Resource):

    def get(self, user_id):
        """ Get user by id and a list of ids of 2nd/3rd degree connections """
        return User(id=user_id).get()


class ConnectionView(Resource):

    def get(self, user_id, target_id):
        """ Check if user id has connections with another user id """
        return User(id=user_id).connections_between(target_id)
