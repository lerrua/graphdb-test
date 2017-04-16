from flask import Flask
from flask_restful import Api

from graphdb_test import views

app = Flask(__name__)
api = Api(app)

# add routes
api.add_resource(views.UserView, '/user/<string:user_id>')


if __name__ == '__main__':
    app.run(debug=True)
