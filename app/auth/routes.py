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

@app.route('/register', methods=['POST','PUT'])
def register():
    if request.method == 'PUT':
        data = request.get_json()
        return str(data)
    try:
        data = request.get_json()
    except Exception as e:
        return "Fail 1", e
    if data:
        username = data.get('username')
        email = data.get('email')
        password = User.password_hash(data.get('password'))
        user = User(username=username, email=email, password=password)
        try:
            db.commit(user)
        except Exception as e:
            return "Fail 2", e
    else:
        return "Fail 3"
