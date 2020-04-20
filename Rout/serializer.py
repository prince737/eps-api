from marshmallow import Schema, fields
from marshmallow.validate import Length

    

class RoutSchema(Schema):
    class Meta:
        fields = ('id', 'value')

rout_schema = RoutSchema()
routs_schema = RoutSchema(many=True)