from flask import render_template, redirect, request, session

from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    
    return render_template('ninjas/ninja.html', dojos= Dojo.get_all())


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    Ninja.create(request.form)
    return redirect('/')