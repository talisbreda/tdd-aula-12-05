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
    
    # Inclusão de funcionário na empresa
    def test_deve_incluir_funcionario(self):
        nome = "Empresa A"
        empresa = Empresa(nome)
        nome_funcionario = "Jorge"
        funcionario = Funcionario(nome_funcionario)

        empresa.incluir_funcionario(funcionario)

        self.assertEqual(empresa.funcionarios[0].nome, funcionario.nome)

    # Criação de projeto
    def test_deve_criar_projeto(self):
        nome_projeto = "Projeto 1"

        projeto = Projeto(nome_projeto)

        self.assertEqual(projeto.nome, nome_projeto)
    
    # Inclusão de projeto na empresa
    def test_deve_incluir_projeto(self):
        nome = "Empresa A"
        empresa = Empresa(nome)
        nome_projeto = "Projeto 1"
        projeto = Projeto(nome_projeto)

        empresa.incluir_projeto(projeto)

        self.assertEqual(empresa.projetos[0].nome, projeto.nome)


if __name__ == '__main__':
    unittest.main()
