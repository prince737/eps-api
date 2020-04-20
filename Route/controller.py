from flask import Blueprint, request, make_response, jsonify, abort
import json
from .models import Route
#from .service import get_all_tests
from setup import db
from .serializer import route_schema
from .serializer import routes_schema


route_controller = Blueprint('route_controller', __name__) 


@route_controller.route("/route_add", methods=['POST']) 
def add_routevalue():
    
    value =request.json['value']

    new_routevalue=Route(value)
    db.session.add(new_routevalue)
    db.session.commit()

    new_routevalue = route_schema.dumps(new_routevalue)

    return new_routevalue



    
   # get_all_tests()


    new_routevalue['status'] = True
    if new_routevalue['status']:
        return new_routevalue, 200 
    else:
        return new_routevalue, 400

@route_controller.route("/route_get", methods=['GET'])
def get_routevalue():
    all_routedata = Route.query.all()
    result= routes_schema.dump(all_routedata)
    print(result)
    return jsonify(result)



@route_controller.route("/route_update/<id>", methods=['PUT'])
def update_routevalue(id):
    try:
        update_this = Route.query.filter_by(id=id).first()
        update_this.value=request.json['value']
        print(update_this.value)
        db.session.commit()
        print(id)
        return {"status": "completed"}, 200
    except Exception as e:
        print(e)
        return {"stauts": "failed"}, 400




@route_controller.route("/route_delete/<id>", methods=['DELETE'])
def delete_routevalue(id):
    try:
        Route.query.filter_by(id=id).delete()
        db.session.commit()
        return {"status": "deleted"}, 200
    except Exception as e:
        print(e)
        return {"stauts": "failed"}, 400
