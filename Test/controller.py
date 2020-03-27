from flask import Blueprint, request, make_response, jsonify, abort
import json
from .models import Test
from .service import get_all_tests

test_controller = Blueprint('test_controller', __name__) 
#Blueprint is a comcept that helps in grouping similar actions in a common place. For eg, we would want all user related endpoints to be handled from a separate module instead of cluttering all in one place. Blueprint makes that possible. 
#The "test_controller" is one such blueprint that separates all "test" related functionality to be handled from this file.


#QUICK (COMMON) RESPONSE CODE RUN DOWN
#200 = Everything is ok, users request was successfully performed
#201 = User asked to store some data, that rewuest was successfully performed.
#400 = Opposite of 200, users request was not successfully performed
#401 = User is not logged in
#403 = User does not access to perform the operation they requested
#500 = General error response code. Mostly used for some unforeseen error. For eg: in generic case of an exception handling block 


@test_controller.route("/test_get")
def profile():
    return jsonify({'key': 'Value'}), 200
    # return {'key': 'Value'}, 200 #This will also work if data is already a dict. But make sure the returned response is always a dictionary. Even for error cases and this its a good practice to use jsonify

@test_controller.route("/test_post", methods=['POST']) #defining /test_post endpoint. "test_post" function will be invoked for the url(endpoint) http://127.0.0.1/test/test_post
def test_post():
    data = json.loads(request.data)
    print(data)
    print(request.data)
    print(data['id']) #assuming is present is request body sent from pastman
    #print(request['id']) #assuming is present is request body sent from pastman. This line will give error saying dict object has no attribute id. Hence the use of json.loads to load data from request object

    #TODO: Perform operation on data which will mostly include db interactions. This logic goes in service.py file.
    get_all_tests()


    data['status'] = True
    if data['status']:
        return jsonify(data), 200 
    else:
        return jsonify(data), 400