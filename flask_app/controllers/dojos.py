from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():

    return redirect ('/dojos')


@app.route('/dojos')
def dojo():

    dojos = Dojo.get_all()

    return render_template ('index.html', dojos = dojos )


@app.route('/ninjas')
def new_ninja():

    dojos = Dojo.get_all()

    return render_template('new_ninja.html', dojos = dojos)


@app.route('/create/ninja', methods=['POST'])
def create_ninja():

    data = { 
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'created_at' : 'NOW()',
        'updated_at' : 'NOW()',
        'dojo_id' : request.form['dojo_id']
    }
    
    Ninja.create(data)

    return redirect('/dojos/' + data['dojo_id'])


@app.route('/create/dojo', methods=['POST'])
def create_dojo():

    data = {
        'name' : request.form['name'],
        'created_at' : 'NOW()',
        'updated_at' : 'NOW()'
    }

    Dojo.create(data)

    return redirect ('/dojos')


@app.route('/dojos/<int:dojo_id>')
def show_ninjas(dojo_id):

    data = {
        'dojo_id' : dojo_id
    }

    ninjas = Ninja.ninjas_in_dojo(data)

    if len(ninjas) < 1:
        return redirect('/dojos')


    return render_template('dojo_show.html', ninjas = ninjas)



