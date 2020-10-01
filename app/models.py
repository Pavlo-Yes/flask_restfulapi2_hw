from app import db, bcrypt


class MoveDb:
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, search_id):
        return cls.query.get(search_id)

    @classmethod
    def update_by_id(cls, update_id, **data):
        cls.query.filter_by(id=update_id).update(data)
        db.session.commit()


class UserModel(db.Model, MoveDb):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, email, password, name):
        self.email = email
        self.password = bcrypt.generate_password_hash(password,12)
        self.name = name

    def __str__(self):
        return f'{self.id}) {self.name}'

    def __repr__(self):
        return f'{self.id}) {self.name}'

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


class PetModel(db.Model, MoveDb):
    __tablename__ = 'pet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    animal_type = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'), nullable=False)

    def __init__(self, name, animal_type, owner_id):
        self.name = name
        self.animal_type = animal_type
        self.owner_id = owner_id


class OwnerModel(db.Model, MoveDb):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(20), nullable=False)
    pets = db.relationship('PetModel', backref='owner', cascade='all, delete', lazy=True)

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
