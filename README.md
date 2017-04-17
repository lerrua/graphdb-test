# GraphDB test

Test application with Neo4J and Python

## Installation

### Dependencies

* Python 3.6
* Neo4J

```
pip install -r dev-requirements.txt
```
or if you have `pip-tools` installed simple do:
```
pip-sync dev-requirements.txt
```

### Configuration

Define database variables
```
export NEO4J_HOST='localhost'
export NEO4J_USERNAME='neo4j'
export NEO4J_PASSWORD='mypass'
```

Populate database
```python
from graphdb_test.models import User

# define a range with data to be generated
User.populate_with_random_data(1, 50000)

# also create index for User.id
User.create_index()

# create some random connections with populated database
User.create_random_connections()
```

#### Running application

Make sure if Neo4J is running and then
```
python api.py
```


### Available endpoints

To get an User with your connections
```
GET http://localhost:5000/user/{user-id}
```

To check if an User have some connection with another User
```
GET http://localhost:5000/connection/{user-id}/{user-id}
```
