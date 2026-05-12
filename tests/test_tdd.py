import sys
import os
_d = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _d)
sys.path.insert(0, os.path.join(os.path.dirname(_d), 'src'))

from empresa import Empresa
import unittest

class TestesTDD(unittest.TestCase):

    # Criação de empresa
    def test_deve_criar_empresa(self):
        nome = "Empresa A"

        empresa = Empresa(nome)

        self.assertEqual(empresa.nome, nome)

if __name__ == '__main__':
    unittest.main()
