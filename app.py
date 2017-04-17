from flask import Flask
from flask_restful import Api

from graphdb_test import views

app = Flask(__name__)
api = Api(app)

# add routes
api.add_resource(views.UserView, '/user/<int:user_id>')
api.add_resource(
    views.ConnectionView, '/connection/<int:user_id>/<int:target_id>')


if __name__ == '__main__':
    app.run(debug=True)
