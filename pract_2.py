''' Practica 2

Nesta tarefa debes empregar Faker para desenvolver un programa que cree os 
datos ficticios de 15 usuarios. Os datos deben almacenarse nun dicionario, de forma que:

Os usuarios estean identificados por un código comprendido entre o número 
1 e o 15. Non poderá haber dous usuarios co mesmo código.
Para cada usuario se almacenen os seguintes datos: nome, dirección, correo 
electrónico, teléfono.

O programa debe mostrar por pantalla os datos de todos os usuarios creados.

Despois, o programa seleccionará aleatoriamente a un dos usuarios para mostrar 
a seguinte mensaxe: "O usuario chamado NOME foi o afortunado!" '''

from faker import Faker
import random 

dato = Faker()
usuarios = {}

for i in range(1, 16):
    usuarios = (i, dato.name(), dato.address(), dato.email(), dato.telephone_number())