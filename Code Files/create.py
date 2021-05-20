from application.models import Positions, Player
from application.forms import PositionForm
from application import db

db.drop_all()

db.create_all()
# Player.__table__.drop()
# Positions.__table__.drop()

posGK = Positions(position='GK') 
posDEF = Positions(position='DEF')
posMID = Positions(position='MID')
posATT = Positions(position='ATT')

db.session.add(posGK)
db.session.add(posDEF)
db.session.add(posMID)
db.session.add(posATT)
db.session.commit()



# use fantasyfootball;

# INSERT INTO positions (position) values ('GK',1);
# INSERT INTO positions (position) values ('DEF',2);
# INSERT INTO positions (position) values ('MID',3);
# INSERT INTO positions (position) values ('ATT',4);

#SELECT * FROM positions;