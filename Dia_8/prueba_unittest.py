import unittest
import cambiar_texto

class TestCambiarTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = cambiar_texto.todo_mayusculas(palabra)

        self.assertEqual(resultado , 'BUEN DIA')


if __name__ == '__main__':
    unittest.main()
