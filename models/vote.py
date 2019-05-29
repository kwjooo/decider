from application import db


class Vote(db.Model):
    __tablename__ = 'vote'

    id = db.Column(db.Integer,
                   primary_key=True)
    participation = db.Column(db.Boolean,
                              unique=False,
                              nullable=False)
    created = db.Column(db.DateTime,
                        unique=False,
                        nullable=False)
    user_id = db.Column(db.String(36),
                        db.ForeignKey('user.id'),
                        nullable=False)
    group_id = db.Column(db.String(36),
                         db.ForeignKey('group.id'),
                         nullable=False)

    category_preferences = db.relationship('CategoryPreference', backref='vote', lazy=True)
