from application import db


class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.String(36),
                   primary_key=True)
    name = db.Column(db.String(30),
                     unique=True,
                     nullable=False)
    address = db.Column(db.String(60),
                        unique=False,
                        nullable=False)
    image_path = db.Column(db.String(60),
                           unique=False,
                           nullable=False,
                           default='default.png')
    map_link = db.Column(db.String(60),
                         unique=False,
                         nullable=False)
    category_id = db.Column(db.Integer,
                            db.ForeignKey('category.id'),
                            nullable=False)

    grades = db.relationship('Grade', backref='restaurant', lazy=True)
    today_restaurants = db.relationship('TodayRestaurant', backref='restaurant', lazy=True)