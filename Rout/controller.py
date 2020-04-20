from flask import Blueprint, request, make_response, jsonify, abort
import json
from .models import Rout
#from .service import get_all_tests
from setup import db
from .serializer import rout_schema
from .serializer import routs_schema


rout_controller = Blueprint('rout_controller', __name__) 


@rout_controller.route("/rout_add", methods=['POST']) 
def add_routvalue():
    
    value =request.json['value']

    new_routvalue=Rout(value)
    db.session.add(new_routvalue)
    db.session.commit()

    new_routvalue = rout_schema.dumps(new_routvalue)

    return new_routvalue



    
   # get_all_tests()


    new_routvalue['status'] = True
    if new_routvalue['status']:
        return new_routvalue, 200 
    else:
        return new_routvalue, 400

@rout_controller.route("/rout_get", methods=['GET'])
def get_routvalue():
    all_routdata = Rout.query.all()
    result= routs_schema.dump(all_routdata)
    print(result)
    return jsonify(result)



@rout_controller.route("/rout_update/<id>", methods=['PUT'])
def update_routvalue(id):
    try:
        update_this = Rout.query.filter_by(id=id).first()
        update_this.value=request.json['value']
        print(update_this.value)
        db.session.commit()
        print(id)
        return {"status": "completed"}, 200
    except Exception as e:
        print(e)
        return {"stauts": "failed"}, 400




@rout_controller.route("/rout_delete/<id>", methods=['DELETE'])
def delete_routvalue(id):
    try:
        Rout.query.filter_by(id=id).delete()
        db.session.commit()
        return {"status": "deleted"}, 200
    except Exception as e:
        print(e)
        return {"stauts": "failed"}, 400
