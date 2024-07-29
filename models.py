from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    county = db.Column(db.String(50), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    animals = db.relationship('Animal', backref='owner', lazy=True)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_email = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)
    price = db.Column(db.Float, nullable=False)
    county = db.Column(db.String(50), nullable=False)
    town = db.Column(db.String(50), nullable=False)
    breed = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    animals = db.relationship('Animal', secondary='order_item', lazy='subquery', backref=db.backref('orders', lazy=True))

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    animals = db.relationship('Animal', secondary='cart_item', lazy='subquery', backref=db.backref('carts', lazy=True))

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)

class Authentication(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    token = db.Column(db.String(255), nullable=False)
