import unittest
import coverage
import os
from Usuarios_test import usuario_admin, usuario_profesor, usuario_alumno


class BaseTestClass(unittest.TestCase):
    @classmethod        
    def setUpClass(cls) -> None:

        # Crear admin
        usuario_admin.crearUsuario()
        usuario_profesor.crearUsuario()
        usuario_alumno.crearUsuario()
        #Logear usuarios
        usuario_admin.logIn()
        usuario_profesor.logIn()
        usuario_alumno.logIn()
        cls.cov = coverage.Coverage()
        cls.cov.start()
        

    @classmethod
    def tearDownClass(cls):
        cls.cov.stop()
        cls.cov.save()
        
        
    def test_dummy(self):
        respuesta = usuario_admin.realizarPeticionGet('/usuarios')
        print(respuesta)
        self.assertEqual(1,1)
if __name__ == '__main__':
    unittest.main()