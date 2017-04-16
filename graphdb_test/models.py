import os
from py2neo import Graph, Node, Relationship


host = os.environ.get('NEO4J_HOST')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')

graph = Graph(host=host, username=username, password=password)

NAMES = ["anna", "andrew", "tom", "leroy", "stenli", "jeff", "jack", "karol"]


class User:

    def __init__(self, id):
        self.id = id

    def get(self):
        user = graph.find_one('User', 'id', self.id)
        return user

    def get_similar_users_by_degree(self, id):
        """ Returns a list of user ids of 2nd/3rd degree connections for a
        particular user id """
        pass

    def connect(self, id1, id2):
        pass

    @staticmethod
    def populate_with_random_data(range_num=100):
        """ Populate database with a defined number of random users """
        query = '''
        WITH {names} AS names_list
        FOREACH (r IN range(1,{range_num}) |
            CREATE (:User {id:r,
                    username:names_list[toInt(size(names_list)*rand())] + r
                    }));
        '''

        return graph.run(query, names=NAMES, range_num=range_num)
