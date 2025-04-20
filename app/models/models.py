from database import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id       = db.Column(db.Integer, primary_key = True)
    email    = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable = False)

    def __init__(self, email, password):
        self.email    = email
        self.password = password

class Roles(db.Model):
    __tablename__ = 'roles'
    id            = db.Column(db.Integer, primary_key = True)
    codigo        = db.Column(db.String(100), nullable=False, unique=True)
    name          = db.Column(db.String(100), nullable=False)
    image         = db.Column(db.String(250), nullable = False)
    route         = db.Column(db.String(100), nullable = False)

    def __init__(self, codigo, name, image, route):
        self.codigo = codigo
        self.name   = name
        self.image  = image
        self.route  = route

class User_has_roles(db.Model):
    __tablename__ = 'user_has_roles'
    id            = db.Column(db.Integer, primary_key = True)
    id_rol        = db.Column(db.Integer, nullable=False)
    id_user       = db.Column(db.Integer, nullable=False)


    def __init__(self, id_user, id_rol):
        self.id_rol  = id_rol
        self.id_user = id_user