from .models import Users
from setup import db, app
from utils.errors import errors
from .serializer import user_schema
from passlib.hash import sha256_crypt
import datetime, os

def register_user(data, image):
    full_name = data.get('full_name')
    phone = data.get('phone')
    dob = datetime.datetime.now()#data.get('dob')
    password = data.get('password')
    gender = data.get('gender')
    email = data.get('email')
    # image = '#'

    try:
        validation = validate_phone_email(phone, email)
        if not validation['status']:
            return validation
        password = sha256_crypt.encrypt(password) #sha256_crypt.verify("password", password)
        img_up = upload_image(image)
        if not img_up[0]['status']:
            return img_up[0]
        user = Users(password, dob, email, full_name, phone, img_up[1], 'patient')
        db.session.add(user)
        db.session.commit()
        db.session.refresh(user)
        
        #fixing format for actual response
        user = user_schema.dumps(user)
        user = user_schema.loads(user)

        return {'status': True, 'user': user}
    except Exception as e:
        print(e)
        os.remove(img_up[1])
        db.session.rollback()
        return {'status': False, 'reason': errors['DEFAULT_ERROR']}

def validate_phone_email(phone, email):
    error_msg = []
    try:
        dupe_email = Users.query.filter_by(email=email).first()
        if dupe_email is not None:
            error_msg.append(errors['EMAIL_IN_USE'])
        dupe_phone = Users.query.filter_by(phone=phone).first()
        if dupe_phone is not None:
            error_msg.append(errors['MOBILE_NUMBER_IN_USE'])
        if len(error_msg):
            return {'status': False, 'reason': error_msg} 
        else:
            return {'status': True}
    except Exception as e:
        print(e)
        return {'status': False, 'reason': errors['DEFAULT_ERROR']}

def upload_image(image):
    try:
        if image:
            filetype = image.filename.split('.')[-1]
            filename = '{}.{}'.format(datetime.datetime.timestamp(datetime.datetime.now()), filetype)
            image.filename = filename
            filepath = os.path.join(app.config['USER_IMAGE_FODLER'], filename)
            image.save(filepath)
            return [{'status': True}, filepath]
    except Exception as e:
        print(e)
        return {'status': False, 'reason': errors['IMAGE_UPLOAD_ERROR']}