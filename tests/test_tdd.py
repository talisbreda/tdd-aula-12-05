import sys
import os
_d = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _d)
sys.path.insert(0, os.path.join(os.path.dirname(_d), 'src'))

from empresa import Empresa
from funcionario import Funcionario
from projeto import Projeto
import unittest

class TestesTDD(unittest.TestCase):

    # Criação de empresa
    def test_deve_criar_empresa(self):
        nome = "Empresa A"

        empresa = Empresa(nome)

        self.assertEqual(empresa.nome, nome)

    # Criação de funcionário
    def test_deve_criar_funcionario(self):
        nome_funcionario = "Jorge"

        funcionario = Funcionario(nome_funcionario)

        self.assertEqual(funcionario.nome, nome_funcionario)
    

if __name__ == '__main__':
    unittest.main()
