
from setup import db

class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String(128), nullable=False)

    def __init__(self, value):
        self.value = value

    def __repr__(self): 
        return '<Route %r>' % self.value
 
#db.create_all