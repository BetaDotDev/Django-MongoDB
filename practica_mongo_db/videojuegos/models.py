from django.db import models
from mongoengine import Document, StringField, ReferenceField, ListField, IntField, FloatField, DateTimeField
import datetime

# Modelo de categoría
class Categoria(Document):
    nombre = StringField(required=True, unique=True) # Nombre de la categoria.
    descripcion = StringField()

    def __str__(self):
        return self.nombre


# Modelo de juego
class Juego(Document):
    titulo = StringField(required=True) # Titulo del juego
    descripcion = StringField() # Pequeña descripcion del juego
    categoria = ReferenceField(Categoria, required=True)  # Aqui hace referencia a lka categoria del jeugo.
    plataforma = StringField()  # Plataforma donde sale el juego
    precio = FloatField(default=0.0) # Precio del juego
    fecha_lanzamiento = DateTimeField(default=datetime.datetime.utcnow), # Fecha de lanzamiento (podemos scarla de steam u otra base de datos)
    puntuacion = IntField(min_value=0, max_value=10) # putuacion methacrytic

    def __str__(self):
        return self.titulo