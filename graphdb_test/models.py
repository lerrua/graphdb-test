import os
from py2neo import Graph


host = os.environ.get('NEO4J_HOST')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')

graph = Graph(host=host, username=username, password=password)

NAMES = ["anna", "andrew", "tom", "leroy", "stenli", "jeff", "jack", "karol"]


class User:

    def __init__(self, id):
        self.id = id

    def get(self):
        """
        Returns a list of user ids of 2nd/3rd degree connections for a
        particular user id
        """

        query = '''
        MATCH p=(u:User)-[:CONNECTED*0..3]-(uu:User)
        WHERE u.id = {id}
        RETURN u as user, collect(uu.id) as ids, count(uu) as total
        LIMIT 5000
        '''
        response = graph.run(query, id=self.id)
        return response.data()

    def connections_between(self, target_id):
        """
        Returns a boolean with result of existence of relationship
        between id and target_id
        """
        response = self.get()
        if response:
            if int(target_id) in response[0]['ids']:
                return True
        return False

    @staticmethod
    def create_index():
        """ Create index for User.id """
        query = 'CREATE INDEX ON :User(id)'
        return graph.run(query)

    @staticmethod
    def create_random_connections():
        """
        Populate actual database with random connections between users
        """
        query = '''
        MATCH (u:User), (s:User)
        WITH u, s
        LIMIT 10000
        WHERE rand() < 0.2
        MERGE (u)-[:CONNECTED]->(s);
        '''
        return graph.run(query)

    @staticmethod
    def populate_with_random_data(range_min=1, range_max=100):
        """ Populate database with a defined number of random users """
        query = '''
        WITH {names} AS names_list
        FOREACH (r IN range({range_min},{range_max}) |
            CREATE (:User {id:r,
                    username:names_list[toInt(size(names_list)*rand())] + r
                    }));
        '''

        return graph.run(
            query, names=NAMES, range_min=range_min, range_max=range_max)
