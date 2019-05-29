from application import db


class CategoryPreference(db.Model):
    __tablename__ = 'category_preference'

    vote_id = db.Column(db.Integer,
                        db.ForeignKey('vote.id'),
                        primary_key=True)
    category_id = db.Column(db.Integer,
                            db.ForeignKey('category.id'),
                            primary_key=True)
    preference = db.Column(db.Integer,
                           unique=False,
                           nullable=False)

