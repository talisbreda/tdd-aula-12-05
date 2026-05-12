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


    def criar_objetos(self):
        nome = "Empresa A"
        empresa = Empresa(nome)
        nome_funcionario = "Jorge"
        funcionario = Funcionario(nome_funcionario)
        nome_projeto = "Projeto 1"
        projeto = Projeto(nome_projeto)
        empresa.incluir_funcionario(funcionario)
        empresa.incluir_projeto(projeto)

        return empresa, funcionario, projeto

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

    # Inclusão de funcionário em projeto
    def test_deve_incluir_funcionario_em_projeto(self):
        empresa, funcionario, projeto = self.criar_objetos()

        empresa.incluir_funcionario_em_projeto(funcionario, projeto)

        self.assertEqual(projeto.funcionarios[0].nome, funcionario.nome)
        self.assertEqual(empresa.projetos[0].funcionarios[0].nome, funcionario.nome)

    # Inclusão de funcionário fora da empresa em projeto
    def test_nao_deve_incluir_funcionario_fora_da_empresa_em_projeto(self):
        empresa, funcionario, projeto = self.criar_objetos()
        nome_funcionario2 = "Pedro"
        funcionario2 = Funcionario(nome_funcionario2)

        empresa.incluir_funcionario_em_projeto(funcionario2, projeto)

        self.assertTrue(len(projeto.funcionarios) == 0)
        self.assertTrue(len(empresa.projetos[0].funcionarios) == 0)

    # Inclusão de funcionário fora da empresa em projeto
    def test_nao_deve_incluir_funcionario_em_projeto_fora_da_empresa(self):
        empresa, funcionario, projeto = self.criar_objetos()
        nome_projeto2 = "projeto 2"
        projeto2 = Projeto(nome_projeto2)

        empresa.incluir_funcionario_em_projeto(funcionario, projeto2)

        self.assertTrue(len(projeto2.funcionarios) == 0)
        self.assertTrue(projeto2 not in empresa.projetos)

if __name__ == '__main__':
    unittest.main()
