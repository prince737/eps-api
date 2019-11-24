from marshmallow import Schema, fields
from marshmallow.validate import Length

class CreateUserSchema(Schema):
    full_name = fields.Str(required=True)
    phone = fields.Str(required=True, validate=Length(equal=10))
    dob = fields.Str(required=True)
    password = fields.Str(required=True)
    gender = fields.Str(required=True)
    email = fields.Str(required=False)
    role = fields.Str(required=False)

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'full_name', 'email', 'phone', 'role', 'gender', 'dob')

user_schema = UserSchema()
users_schema = UserSchema(many=True)