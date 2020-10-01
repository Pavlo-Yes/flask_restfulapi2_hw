from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class UserSchema(Schema):
    id = fields.Integer()
    email = fields.Email(required=True)
    password = fields.String(validate=Length(6, 255, error='password must be 6-255 characters'), required=True)
    name = fields.String(validate=Length(2, 20, error='name must be 2-20 characters'), required=True)


class PetSchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=Length(2, 20, error='name must be 2-20 characters'), required=True)
    animal_type = fields.String(validate=Length(2, 20, error='type must be 2-20 characters'), required=True)
    owner_id = fields.Integer(required=True)


class OwnerSchema(Schema):
    id = fields.Integer()
    name = fields.String(validate=Length(2, 20, error='name must be 2-20 characters'), required=True)
    age = fields.Integer(validate=Range(6, 120, error='age must be 6-120'), required=True)
    city = fields.String(validate=Length(2, 20, error='name must be 2-20 characters'), required=True)
