from itsdangerous import json
from app import app, db
from flask import request, render_template, jsonify, url_for
from app.models import User

@app.route('/',methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

@app.route('/<int:var>', methods=['GET','POST'])
def count(var):
    data = {
        'id': var
    }
    result = jsonify(data)
    return render_template('number.html', result, text= f"The given number is : {id} ")

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"error": e})
    if data:
        username = data['username']
        email = data.get('email')
        password = data.get('password')
        user = User(username=username, email=email, password_hash=password)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return "Fail 2"
        return jsonify({"message":"Registration complete"})
    else:
        return jsonify({"message":"Something went wrong..."})
