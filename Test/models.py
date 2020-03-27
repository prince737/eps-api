#create models for test to test database functionality
from setup import db

class Test(db.Model): #test table definitions
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value1 = db.Column(db.String(512), nullable=False)
    value2 = db.Column(db.String(512), nullable=False)

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __repr__(self): #this is what you get if you print Test Object
        return '<Test %r>' % self.value1
