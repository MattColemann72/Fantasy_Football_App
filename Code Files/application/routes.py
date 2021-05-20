from itertools import count
from operator import pos
from flask import render_template, url_for, redirect, request
from jinja2.utils import pformat
from application import app, db
from application.models import Player, Positions
from application.forms import PlayerForm, PositionForm


@app.route('/', methods=['POST', 'GET'])
def index():
    pname = Player.query.all()
    count = 0
    if Player.query.count() < 1:
        count = 0
    else:
        count = 1
    return render_template('index.html', title="Football Squad", pname=pname, count=count)


@app.route('/add', methods=['POST', 'GET'])
def add():
    pform = PlayerForm()
    posform = PositionForm()
    #ppos = Positions(id = Player.id)
    if pform.validate_on_submit():
        pname = Player(name = pform.name.data, position_id = 1)
#        ppos = Player(position = posform.position.data)
        #get position_id from Player class
        # playerpositionid = Player.position_id
        # playerpositionid = 1
        #db.session.add(ppos)
        db.session.add(pname)
        db.session.commit()
        #return redirect(url_for('index'))
    #posform = PositionForm.position
    return render_template('add.html', title="Add A New Player", pform=pform, posform=posform)


@app.route('/squad', methods=['POST', 'GET'])
def squad():
    return render_template('squads.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    pform = PlayerForm()
    posform = PositionForm()
    posselect = posform.position
    playerpos = Positions.position
    pname = Player.query.get(id)
    if pform.validate_on_submit():
        pname.name = pform.name.data
        db.session.commit()
        #return redirect(url_for('index'))
    elif request.method == 'GET':
        pform.name.data = pname.name
    # if posform.validate_on_submit():
    #     for i in posform.query.all():



    #playerpos.query()

    return render_template('update.html', title='Update A Player', pform=pform, posselect=posselect, posform=posform, playerpos=playerpos)


@app.route('/delete/<int:id>')
def delete(id):
    pname = Player.query.get(id)
    db.session.delete(pname)
    db.session.commit()
    return redirect(url_for('index'))