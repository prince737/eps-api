from marshmallow import Schema, fields
from marshmallow.validate import Length

    

class TestSchema(Schema):
    class Meta:
        fields = ('id', 'value1','value2')

test_schema = TestSchema()
tests_schema = TestSchema(many=True)