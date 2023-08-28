from testing_client import BaseTestClass, usuario_admin


class TestUsuarios(BaseTestClass):
    
    def test_dummy(self):
        respuesta = usuario_admin.realizarPeticionGet('/usuarios')
        print(respuesta)
        self.assertEqual(1,1)