from faker import Faker
import random

dato = Faker()
usuarios = {}


for user_id in range(1, 16):
    nombre = dato.name()
    direccion = dato.address()
    email = dato.email()
    telf = dato.phone_number()
    usuarios[user_id] = {
        'nombre': nombre,
        'direccion': direccion,
        'email': email,
        'telf': telf
    }

print(usuarios)

elegido = (random.randrange(1, 16))
ganador = usuarios.get(elegido)
print(f'"El usuario con nombre: {ganador['nombre']} es el afortunado!!')