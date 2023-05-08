from . import bp as app
from flask import request, make_response, jsonify
from flask_cors import CORS, cross_origin
from app.blueprints.social.models import User

@app.route('/signin', methods=['GET','POST'])
def api_signin():
    email = request.json.get('email')
    password = request.json.get('password')
    print(email,password)
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        print(user.token)
        print(str(user.token))
        return jsonify({
            'token':user.token,
            'username':user.username
            }), 200

    return jsonify({'error':"Invalid User info"}), 400