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


    def criar_empresa_com_funcionario_e_projeto(self):
        nome_empresa_a = "Empresa A"
        empresa_a = Empresa(nome_empresa_a)
        nome_jorge = "Jorge"
        jorge = Funcionario(nome_jorge)
        nome_projeto_1 = "Projeto 1"
        projeto_1 = Projeto(nome_projeto_1)
        empresa_a.incluir_funcionario(jorge)
        empresa_a.incluir_projeto(projeto_1)

        return empresa_a, jorge, projeto_1

    def criar_empresa_com_funcionario_alocado_em_projeto(self):
        nome_empresa_a = "Empresa A"
        empresa_a = Empresa(nome_empresa_a)
        nome_jorge = "Jorge"
        jorge = Funcionario(nome_jorge)
        nome_projeto_1 = "Projeto 1"
        projeto_1 = Projeto(nome_projeto_1)
        empresa_a.incluir_funcionario(jorge)
        empresa_a.incluir_projeto(projeto_1)
        empresa_a.incluir_funcionario_em_projeto(jorge, projeto_1)

        return empresa_a, jorge, projeto_1

    def criar_empresa(self):
        nome_empresa_a = "Empresa A"
        empresa_a = Empresa(nome_empresa_a)
        return empresa_a

    # Criação de empresa
    def test_deve_criar_empresa(self):
        nome_empresa_a = "Empresa A"

        empresa_a = Empresa(nome_empresa_a)

        self.assertEqual(empresa_a.nome, nome_empresa_a)

    # Criação de funcionário
    def test_deve_criar_funcionario(self):
        nome_jorge = "Jorge"

        jorge = Funcionario(nome_jorge)

        self.assertEqual(jorge.nome, nome_jorge)

    # Inclusão de funcionário na empresa
    def test_deve_incluir_funcionario(self):
        nome_empresa_a = "Empresa A"
        empresa_a = Empresa(nome_empresa_a)
        nome_jorge = "Jorge"
        jorge = Funcionario(nome_jorge)

        empresa_a.incluir_funcionario(jorge)

        self.assertEqual(empresa_a.funcionarios[0].nome, jorge.nome)

    # Criação de projeto
    def test_deve_criar_projeto(self):
        nome_projeto_1 = "Projeto 1"

        projeto_1 = Projeto(nome_projeto_1)

        self.assertEqual(projeto_1.nome, nome_projeto_1)

    # Inclusão de projeto na empresa
    def test_deve_incluir_projeto(self):
        nome_empresa_a = "Empresa A"
        empresa_a = Empresa(nome_empresa_a)
        nome_projeto_1 = "Projeto 1"
        projeto_1 = Projeto(nome_projeto_1)

        empresa_a.incluir_projeto(projeto_1)

        self.assertEqual(empresa_a.projetos[0].nome, projeto_1.nome)

    # Inclusão de funcionário em projeto
    def test_deve_incluir_funcionario_em_projeto(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_e_projeto()

        empresa_a.incluir_funcionario_em_projeto(jorge, projeto_1)

        self.assertEqual(projeto_1.funcionarios[0].nome, jorge.nome)
        self.assertEqual(empresa_a.projetos[0].funcionarios[0].nome, jorge.nome)

    # Inclusão de funcionário fora da empresa em projeto
    def test_nao_deve_incluir_funcionario_fora_da_empresa_em_projeto(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_e_projeto()
        nome_pedro = "Pedro"
        pedro = Funcionario(nome_pedro)

        empresa_a.incluir_funcionario_em_projeto(pedro, projeto_1)

        self.assertTrue(len(projeto_1.funcionarios) == 0)
        self.assertTrue(len(empresa_a.projetos[0].funcionarios) == 0)

    # Inclusão de funcionário fora da empresa em projeto
    def test_nao_deve_incluir_funcionario_em_projeto_fora_da_empresa(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_e_projeto()
        nome_projeto_2 = "projeto 2"
        projeto_2 = Projeto(nome_projeto_2)

        empresa_a.incluir_funcionario_em_projeto(jorge, projeto_2)

        self.assertTrue(len(projeto_2.funcionarios) == 0)
        self.assertTrue(projeto_2 not in empresa_a.projetos)

    # Inclusão de vários funcionários na empresa
    def test_deve_incluir_varios_funcionarios_na_empresa(self):
        empresa_a = self.criar_empresa()
        nome_pedro = "Pedro"
        pedro = Funcionario(nome_pedro)
        nome_joao = "João"
        joao = Funcionario(nome_joao)
        nome_carlos = "Carlos"
        carlos = Funcionario(nome_carlos)
        funcionarios = [pedro, joao, carlos]

        empresa_a.incluir_funcionarios(funcionarios)

        self.assertTrue(len(empresa_a.funcionarios) == 3)
        self.assertTrue(pedro in empresa_a.funcionarios)
        self.assertTrue(joao in empresa_a.funcionarios)
        self.assertTrue(carlos in empresa_a.funcionarios)

    # Inclusão de vários projetos na empresa
    def test_deve_incluir_varios_projetos_na_empresa(self):
        empresa_a = self.criar_empresa()
        nome_projeto_pedro = "Pedro"
        projeto_pedro = Projeto(nome_projeto_pedro)
        nome_projeto_joao = "João"
        projeto_joao = Projeto(nome_projeto_joao)
        nome_projeto_carlos = "Carlos"
        projeto_carlos = Projeto(nome_projeto_carlos)
        projetos = [projeto_pedro, projeto_joao, projeto_carlos]

        empresa_a.incluir_projetos(projetos)

        self.assertTrue(len(empresa_a.projetos) == 3)
        self.assertTrue(projeto_pedro in empresa_a.projetos)
        self.assertTrue(projeto_joao in empresa_a.projetos)
        self.assertTrue(projeto_carlos in empresa_a.projetos)

    # Inclusão de funcionário em vários projetos
    def test_deve_incluir_funcionario_em_varios_projetos(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_e_projeto()
        nome_projeto_2 = "projeto 2"
        projeto_2 = Projeto(nome_projeto_2)
        empresa_a.incluir_projeto(projeto_2)
        projetos = [projeto_1, projeto_2]

        empresa_a.incluir_funcionario_em_projetos(jorge, projetos)

        self.assertTrue(jorge in projeto_1.funcionarios)
        self.assertTrue(jorge in projeto_2.funcionarios)

    # Inclusão de funcionário repetido na empresa
    def test_nao_deve_incluir_funcionario_repetido(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_e_projeto()

        empresa_a.incluir_funcionario(jorge)

        self.assertTrue(len(empresa_a.funcionarios) == 1)
        self.assertTrue(jorge in empresa_a.funcionarios)

    # Inclusão de projeto repetido na empresa
    def test_nao_deve_incluir_projeto_repetido(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_e_projeto()

        empresa_a.incluir_projeto(projeto_1)

        self.assertTrue(len(empresa_a.projetos) == 1)
        self.assertTrue(projeto_1 in empresa_a.projetos)

    # Inclusão de funcionário repetido em projeto
    def test_nao_deve_incluir_funcionario_repetido_em_projeto(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_alocado_em_projeto()

        empresa_a.incluir_funcionario_em_projeto(jorge, projeto_1)

        self.assertTrue(len(projeto_1.funcionarios) == 1)
        self.assertTrue(jorge in projeto_1.funcionarios)

if __name__ == '__main__':
    unittest.main()
