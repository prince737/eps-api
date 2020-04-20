from marshmallow import Schema, fields
from marshmallow.validate import Length

    

class RouteSchema(Schema):
    class Meta:
        fields = ('id', 'value')

route_schema = RouteSchema()
routes_schema = RouteSchema(many=True)