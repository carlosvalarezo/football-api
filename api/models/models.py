from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class League(db.Model):
    __tablename__ = 'leagues'
    league_id = db.Column(db.Integer, primary_key=True)
    league_name = db.Column(db.String)
    league_country = db.Column(db.String)

    # def __init__(self, name, country):
    #     self.name = name
    #     self.country = country

    def insert(self):
        db.session.add(self)
        db.session.commit()
