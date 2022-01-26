from app import app
from flask import request, render_template, jsonify

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
    return jsonify(data)