from flask import Blueprint, request, make_response, jsonify, abort
from .models import Users
from flask_login import login_user, login_required, current_user, logout_user
from .serializer import CreateUserSchema
from .service import register_user

user_controller = Blueprint('user_controller', __name__)
create_user_schema = CreateUserSchema()

@user_controller.route("/login", methods=['POST'])
def login():
    user = Users.query.filter_by(name='Prince Dey').first()
    login_user(user)
    return 'You are logged in.'

@user_controller.route("/register", methods=['POST'])
def register():
    if 'user_image' in request.files:
        image = request.files['user_image']
    data = request.form
    errors = create_user_schema.validate(data)
    if errors:
        res = {}
        res['status'] = False
        res['reason'] = errors
        return jsonify(res), 400
    status = register_user(data, image)
    if status['status']:
        return jsonify(status), 200
    else:
        return jsonify(status), 400

@user_controller.route("/verify_phone")
def verify_phone():
    res = {'status': 'success'}
    return jsonify(res), 200

@user_controller.route("/verify_email")
def verify_email():
    res = {'status': 'success'}
    return jsonify(res), 200

@user_controller.route("/profile")
@login_required
def profile():
    return 'hello '+current_user.name

@user_controller.route("/logout")
@login_required
def logout():
    logout_user()
    return 'logged out'