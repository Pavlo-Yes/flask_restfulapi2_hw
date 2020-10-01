from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt import JWT

from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
api = Api(app)
bcrypt = Bcrypt()

from security import identity, authenticate

JWT(app, authenticate, identity)

from app.resources import UserResource, OwnerResource, PetResource

api.add_resource(UserResource, '/user', '/user/<int:user_id>')
api.add_resource(OwnerResource, '/owner', '/owner/<int:owner_id>')
api.add_resource(PetResource, '/pets', '/owner/<int:owner_id>/pets', '/pet/<int:pet_id>')
