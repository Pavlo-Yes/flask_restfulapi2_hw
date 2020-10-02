from flask_restful import Resource, request
from flask_jwt import jwt_required

from app.schemas import UserSchema, OwnerSchema, PetSchema
from app.models import UserModel, OwnerModel, PetModel


class UserResource(Resource):
    def get(self):
        users = UserModel.query.all()
        schema = UserSchema()
        return schema.dump(users, many=True), 200

    def post(self):
        candidate = request.get_json()
        schema = UserSchema()
        errors = schema.validate(candidate)
        if errors:
            return {'massage': errors}, 400
        data = schema.dump(candidate)
        if UserModel.find_by_email(data['email']):
            return {'massage': 'this mail already exist'}, 400
        user = UserModel(**data)

        user.save_to_db()
        return {'massage': 'User has been created'}, 201

    @jwt_required()
    def patch(self, user_id):
        UserModel.update_by_id(user_id, **request.get_json())
        return {'massage': 'User has been update'}, 200

    @jwt_required()
    def delete(self, user_id):
        delete_user = UserModel.find_by_id(user_id)
        if delete_user:
            UserModel.delete_from_db(delete_user)
            return {'massage': 'User has been deleted'}, 200
        return {'massage': 'bad id'}, 400


class OwnerResource(Resource):
    def get(self, **kwargs):
        schema = OwnerSchema()
        if kwargs:
            owner = OwnerModel.find_by_id(kwargs['owner_id'])
            return schema.dump(owner), 200
        owners = OwnerModel.query.all()
        return schema.dump(owners, many=True), 200

    @jwt_required()
    def post(self):
        candidate = request.get_json()
        schema = OwnerSchema()
        errors = schema.validate(candidate)
        if errors:
            return {'massage': errors}, 400
        data = schema.dump(candidate)
        owner = OwnerModel(**data)
        owner.save_to_db()
        return {'massage': 'Owner has been created'}, 201

    @jwt_required()
    def patch(self, owner_id):
        OwnerModel.update_by_id(owner_id, **request.get_json())
        return {'massage': 'Owner has been update'}, 200

    @jwt_required()
    def delete(self, owner_id):
        delete_owner = OwnerModel.find_by_id(owner_id)
        if delete_owner:
            OwnerModel.delete_from_db(delete_owner)
            return {'massage': 'Owner has been deleted'}, 200
        return {'massage': 'bad id'}, 400


class PetResource(Resource):
    def get(self, **kwargs):
        schema = PetSchema()
        if kwargs:
            pet = PetModel.find_by_id(kwargs['pet_id'])
            return schema.dump(pet), 200
        pets = PetModel.query.all()
        return schema.dump(pets, many=True), 200

    @jwt_required()
    def post(self, owner_id):
        candidate = request.get_json()
        owner = OwnerModel.query.get(owner_id)
        if not owner:
            return {'message': 'user not found'}, 404
        schema = PetSchema()
        errors = schema.validate(candidate)
        if errors:
            return {'massage': errors}, 400
        data = schema.dump(candidate)
        pet = PetModel(**data)
        owner.pets.append(pet)
        owner.save_to_db()
        return {'massage': 'pet has been added'}, 201

    @jwt_required()
    def patch(self, pet_id):
        PetModel.update_by_id(pet_id, **request.get_json())
        return {'massage': 'Pet has been update'}, 200

    @jwt_required()
    def delete(self, pet_id):
        delete_pet = PetModel.find_by_id(pet_id)
        if delete_pet:
            PetModel.delete_from_db(delete_pet)
            return {'massage': 'Pet has been deleted'}, 200
        return {'massage': 'bad id'}, 400
