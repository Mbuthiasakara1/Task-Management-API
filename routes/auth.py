from flask import Blueprint,request,jsonify
from models import db,User
from utils.auth_helpers import hash_password,verify_password
from utils.validators import is_valid_email,is_strong_password
from flask_jwt_extended import create_access_token


#create bluebrint for auth routes

auth_bp=Blueprint('auth',__name__,url_prefix='/api/auth')

@auth_bp.route('/register',methods=['POST'])
def register():
    """
    Register a new user
    """
    #get data
    data=request.get_json()
    email=data.get('email')
    username=data.get('username')
    password=data.get('password')

    if not email or not username or not password:
        return jsonify({"error":"Email,username, and password are required"})
    
    if not is_valid_email(email):
        return jsonify({"error":"Invalid email format"}),400
    

    is_valid,message=is_strong_password(password)

    if not is_valid:
        return jsonify({"error":message}),400
    

    existing_user=User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({"error":"User with this email already exists"}),409
    

    #hash the password

    hashed_password=hash_password(password)


    #create new user

    new_user =User(
        email=email,
        username=username,
        password=hashed_password
    )


  #save to database
    db.session.add(new_user)

    db.session.commit()


    #response


    return jsonify({
        "message":"User registered successfully",

        "user":new_user.to_dict()
    }),201


@auth_bp.route('/login',methods=['POST'])

def login():
    """Login user and return token"""

    #get data from request

    data=request.get_json()
    email=data.get('email')
    password=data.get('password')


    #check if both fields are provided
    if not email or not password:
        return jsonify({"error":"Email and password are required"}),400
    
    # find user by email
    user=User.query.filter_by(email=email).first()



    #check if user exists

    if not user:
        return jsonify({"error":"Invalid email or password"}),401
    

     # Verify password
    if not verify_password(password, user.password):
        return jsonify({"error": "Invalid email or password"}), 401
    
    #create token

    token=create_access_token(identity=user.id)


    return jsonify({
        "message":"login succesful",
        "token":token,
        "user":user.to_dict()
        
    }),200



    
