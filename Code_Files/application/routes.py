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
    # count = 0
    # if Player.query.count() < 1:
    #     count = 0
    # else:
    #     count = 1
    return render_template('index.html', title="Football Squad", pname=pname)


@app.route('/add', methods=['POST', 'GET'])
def add():
    pform = PlayerForm()
    posform = PositionForm()
    pos_id = 1

    if pform.validate_on_submit():
        pname = Player( name = pform.name.data, position_id = pos_id )
        db.session.add(pname)
        db.session.commit()

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
    posid = Player.position_id
    position = Positions.query.get(id)
    posid = Positions.id

    print(Positions.query.all())

    if pform.validate_on_submit():
        pname.name = pform.name.data
        # position.player = posform.position.data
        # #Player.position_id = posform.position.data
        # position.position = posform.position.data

        # print(position)

        # if position.position == "Goalkeeper":
        #     position = 0
        # elif position.position == "Defender":
        #     position = 1
        # elif position.position == "Midfielder":
        #     position = 2
        # elif position.position == "Attacker":
        #     position = 3
        
        #print(posid)
        #db.session.add(posid)
        db.session.commit()
    

    elif request.method == 'GET':
        pform.name.data = pname.name

    return render_template('update.html', title='Update A Player', pform=pform, posselect=posselect, posform=posform, playerpos=playerpos, posid=posid, position=position)


@app.route('/delete/<int:id>')
def delete(id):
    pname = Player.query.get(id)
    db.session.delete(pname)
    db.session.commit()
    return redirect(url_for('index'))