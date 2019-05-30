from application import db
from constants import LUNCH_TIME, DINNER_TIME

groups_restaurants = db.Table('groups_restaurants',
                              db.Column('group_id', db.String(36), db.ForeignKey('group.id'), primary_key=True),
                              db.Column('restaurant_id', db.String(36), db.ForeignKey('restaurant.id'),
                                        primary_key=True)
                              )


class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.String(36),
                   primary_key=True)
    name = db.Column(db.String(16),
                     unique=True,
                     nullable=False)
    address = db.Column(db.String(60),
                        unique=False,
                        nullable=False)
    lunch_time = db.Column(db.Time,
                           unique=False,
                           nullable=False,
                           default=LUNCH_TIME)
    dinner_time = db.Column(db.Time,
                            unique=False,
                            nullable=False,
                            default=DINNER_TIME)

    restaurants = db.relationship('Restaurant', secondary=groups_restaurants, lazy='subquery',
                                  backref=db.backref('groups', lazy=True))
    today_restaurants = db.relationship('TodayRestaurant', backref='group', lazy=True)
    votes = db.relationship('Vote', backref='group', lazy=True)
