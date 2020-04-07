from flask import Blueprint, request, make_response, jsonify, abort
import json
from .models import Test
from .service import get_all_tests
from setup import db
from .serializer import test_schema
from .serializer import tests_schema


test_controller = Blueprint('test_controller', __name__) 


@test_controller.route("/test_post", methods=['POST']) 
def add_testvalue():
    
    value1 =request.json['value1']
    value2 =request.json['value2']

    new_testvalue=Test(value1,value2)
    db.session.add(new_testvalue)
    db.session.commit()

    new_testvalue = test_schema.dumps(new_testvalue)

    return new_testvalue



    
    get_all_tests()


    new_testvalue['status'] = True
    if new_testvalue['status']:
        return new_testvalue, 200 
    else:
        return new_testvalue, 400

@test_controller.route("/test_get", methods=['GET'])
def get_testvalue():
    all_testdata = Test.query.all()
    result= tests_schema.dump(all_testdata)
    print(result)
    return jsonify(result)



@test_controller.route("/test_update/<id>", methods=['PUT'])
def update_testvalue(id):
    try:
        update_this = Test.query.filter_by(id=id).first()
        update_this.value2=request.json['value2']
        print(update_this.value2)
        db.session.commit()
        print(id)
        return {"status": "completed"}, 200
    except Exception as e:
        print(e)
        return {"stauts": "failed"}, 400




@test_controller.route("/test_delete/<id>", methods=['DELETE'])
def delete_testvalue(id):
    try:
        Test.query.filter_by(id=id).delete()
        db.session.commit()
        return {"status": "deleted"}, 200
    except Exception as e:
        print(e)
        return {"stauts": "failed"}, 400
