from flask_marshmallow import Marshmallow 

ma = Marshmallow()

#ESQUEMA DE USUARIO

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password')

class rolesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'codigo', 'name', 'image', 'route')