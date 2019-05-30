from application import db
from werkzeug.security import generate_password_hash, check_password_hash

users_groups = db.Table('users_groups',
                        db.Column('user_id', db.String(36), db.ForeignKey('user.id'), primary_key=True),
                        db.Column('group_id', db.String(36), db.ForeignKey('group.id'), primary_key=True)
                        )


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String(36),
                   primary_key=True)
    user_id = db.Column(db.String(30),
                        unique=True,
                        nullable=False)
    password = db.Column(db.String(32),
                         unique=False,
                         nullable=False)
    nickname = db.Column(db.String(16),
                         unique=True,
                         nullable=False)
    access_token = db.Column(db.String(36),
                             unique=False,
                             nullable=True)
    token_expired = db.Column(db.DateTime,
                              unique=False,
                              nullable=True)

    groups = db.relationship('Group', secondary=users_groups, lazy='subquery',
                             backref=db.backref('users', lazy=True))
    grades = db.relationship('Grade', backref='user', lazy=True)
    votes = db.relationship('Vote', backref='user', lazy=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

        self.set_password(kwargs['password'])

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
