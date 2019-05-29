from application import db


class Grade(db.Model):
    __tablename__ = 'grade'

    id = db.Column(db.Integer,
                   primary_key=True)
    grade = db.Column(db.Integer,
                      unique=False,
                      nullable=False)
    created = db.Column(db.DateTime,
                        unique=False,
                        nullable=False)
    user_id = db.Column(db.String(36),
                        db.ForeignKey('user.id'),
                        nullable=False)
    restaurant_id = db.Column(db.String(36),
                              db.ForeignKey('restaurant.id'),
                              nullable=False)