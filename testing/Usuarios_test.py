import requests
import json
import os


    
class UsuariosTesting():


    def __init__(self, rol, dni, email, contrasegna) -> None:
        self.rol = rol
        self.email = email
        self.dni = dni
        self.contrasegna = contrasegna
        self.atributos = []
        self.token = ""

    def setAtributos(self, atributos):
        self.atributos = atributos

    def getAtributos(self):
        return self.atributos


    def realizarPeticionPost(endpoint, data):
        try:
            url = 'http://127.0.0.1:' +os.get('PORT')+ endpoint
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, headers=headers, data=json.dumps(data))
            return response.json()
        except Exception as e:
            print(e)
            return f'No se realizo la petición {endpoint} \nError {e}'
    def realizarPeticionGet(endpoint):
        try:
            url = 'http://127.0.0.1:' +os.get('PORT')+ endpoint
            headers = {'Content-Type': 'application/json'}
            response = requests.get(url, headers=headers)
            return response.json()
        except Exception as e:
            print(e)
            return f'No se realizo la petición {endpoint} \nError {e}'
    
    def logIn(self):
        try:
            response = self.realizarPeticionPost('/auth/login', {"email": self.email, "contrasegna": self.contrasegna})
            self.token = response['access_token']
            return response['access_token']
        except Exception as e:
            print(e)
            return ""
    
    def crearUsuario(self):
        try:
            data = {
                "dni" : self.dni,
                "nombre": self.atributos['nombre'],
                "apellido": self.atributos['apellido'], 
                "email": self.email,
                "fecha_nacimiento": self.atributos['fecha_nacimiento'],
                "estado" : self.atributos['estado'],
                "rol": self.rol,
                "nombre_usuario": self.atributos['nombre_usuario'],
                "contrasegna": self.contrasegna
                }
            if self.rol =="alumno":
                data['altura'] = self.atributos['altura']
                data['peso'] = self.atributos['peso']
            elif self.rol == "profesor":
                data['especialidad'] = self.atributos['especialidad']
                data['salario'] = self.atributos['salario']
            response = self.realizarPeticionPost('/auth/register', data)
            return response
        except Exception as e:
            print(e)
            return f'No se realizco el registro del usuario \nError {e}'
        

usuario_admin = UsuariosTesting(
    "admin", 
    os.getenv('ADMIN_DNI'),
    os.getenv('ADMIN_EMAIL'),
    "admin")
usuario_admin.setAtributos({
    "nombre": "admin",
    "apellido": "admin",
    "fecha_nacimiento": "1999-01-01",
    "estado": True,
    "nombre_usuario": os.getenv('ADMIN_USERNAME')
})
usuario_profesor = UsuariosTesting(
    "profesor", 
    12346578,
    "profesor@example.com",
    "profesor")
usuario_profesor.setAtributos({
    "nombre": "profesor",
    "apellido": "profesor",
    "fecha_nacimiento": "1999-01-01",
    "estado": True,
    "nombre_usuario": "profesor",
    "especialidad": "Musculacion",
    "salario": 10000
})
usuario_alumno = UsuariosTesting(
    "alumno", 
    87654321,
    "alumno@example.com",
    "alumno")
usuario_alumno.setAtributos({
    "nombre": "alumno",
    "apellido": "alumno",
    "fecha_nacimiento": "1999-01-01",
    "estado": True,
    "nombre_usuario": "alumno",
    "altura": 1.80,
    "peso": 80
})



