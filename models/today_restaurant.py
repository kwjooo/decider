from application import db


class TodayRestaurant(db.Model):
    __tablename__ = 'today_restaurant'

    id = db.Column(db.Integer,
                   primary_key=True)
    created = db.Column(db.DateTime,
                        unique=False,
                        nullable=False)
    group_id = db.Column(db.String(36),
                         db.ForeignKey('group.id'),
                         nullable=False)
    restaurant_id = db.Column(db.String(36),
                              db.ForeignKey('restaurant.id'),
                              nullable=False)
