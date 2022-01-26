from app import app
from flask import request, render_template

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

@app.route('/<int:var>', methods=['GET','POST'])
def count(var):
    return f"This was on the url : {var}"