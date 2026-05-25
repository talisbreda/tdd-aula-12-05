import sys
import os
_d = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _d)
sys.path.insert(0, os.path.join(os.path.dirname(_d), 'src'))

from empresa import Empresa
from funcionario import Funcionario
from projeto import Projeto
from ocorrencia import Ocorrencia, EstadoEnum, LimiteOcorrenciasPorFuncionarioAtingidoException
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

    def criar_ocorrencia_com_funcionario_atribuido(self):
        nome_empresa_a = "Empresa A"
        empresa_a = Empresa(nome_empresa_a)
        nome_jorge = "Jorge"
        jorge = Funcionario(nome_jorge)
        nome_projeto_1 = "Projeto 1"
        projeto_1 = Projeto(nome_projeto_1)
        empresa_a.incluir_funcionario(jorge)
        empresa_a.incluir_projeto(projeto_1)
        empresa_a.incluir_funcionario_em_projeto(jorge, projeto_1)
        ocorrencia_bug = projeto_1.cria_ocorrencia("bugTeste")
        projeto_1.atribuir_funcionario_a_ocorrencia(jorge, ocorrencia_bug)

        return empresa_a, jorge, projeto_1, ocorrencia_bug

    def criar_dez_ocorrencias_atribuidas_ao_funcionario(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_alocado_em_projeto()
        ocorrencias = []
        for i in range(10):
            nova_ocorrencia = projeto_1.cria_ocorrencia("Ocorrencia " + str(i))
            ocorrencias.append(nova_ocorrencia)
            projeto_1.atribuir_funcionario_a_ocorrencia(jorge, nova_ocorrencia)

        return empresa_a, jorge, projeto_1, ocorrencias


    def criar_empresa(self):
        nome_empresa_a = "Empresa A"
        empresa_a = Empresa(nome_empresa_a)
        return empresa_a

    # Criação de ocorrencia
    def test_cria_ocorrencia(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_alocado_em_projeto()

        ocorrencia_bug = projeto_1.cria_ocorrencia("bugTeste")

        self.assertTrue(ocorrencia_bug in projeto_1.ocorrencias)


    # Atribui funcionario a ocorrência
    def test_atribui_funcionario_ocorrencia(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_alocado_em_projeto()
        ocorrencia_bug = projeto_1.cria_ocorrencia("bugTeste")

        ocorrencia_bug.atribuir_funcionario(jorge)

        self.assertEqual(ocorrencia_bug.funcionario, jorge)

    def test_atribui_funcionario_fora_do_projeto_em_ocorrencia(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_e_projeto()
        ocorrencia_bug = projeto_1.cria_ocorrencia("bugTeste")

        projeto_1.atribuir_funcionario_a_ocorrencia(jorge, ocorrencia_bug)

        self.assertNotEqual(ocorrencia_bug.funcionario, jorge)

    def test_ultimo_funcionario_ocorrencia(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_alocado_em_projeto()
        pedro = Funcionario("Pedro")
        empresa_a.incluir_funcionario(pedro)
        projeto_1.incluir_funcionario(pedro)
        ocorrencia_bug = projeto_1.cria_ocorrencia("bugTeste")
        ocorrencia_bug.atribuir_funcionario(jorge)

        ocorrencia_bug.atribuir_funcionario(pedro)

        self.assertEqual(ocorrencia_bug.funcionario, pedro)

    def test_identificador_unico(self):
        empresa_a, jorge, projeto_1 = self.criar_empresa_com_funcionario_e_projeto()
        primeira_ocorrencia_bug = projeto_1.cria_ocorrencia("bugTeste")
        segunda_ocorrencia_bug = projeto_1.cria_ocorrencia("bugTeste")

        self.assertNotEqual(primeira_ocorrencia_bug.id, segunda_ocorrencia_bug.id)

    def test_ocorrencia_aberta(self):
        empresa_a, jorge, projeto_1, ocorrencia_bug = self.criar_ocorrencia_com_funcionario_atribuido()

        self.assertTrue(ocorrencia_bug.estado == EstadoEnum.ABERTO)

    def test_concluir_ocorrencia(self):
        empresa_a, jorge, projeto_1, ocorrencia_bug = self.criar_ocorrencia_com_funcionario_atribuido()

        ocorrencia_bug.fechar()

        self.assertTrue(ocorrencia_bug.estado == EstadoEnum.FECHADO)

    def test_altera_prioridade_ocorrencia_aberta(self):
        empresa_a, jorge, projeto_1, ocorrencia_bug = self.criar_ocorrencia_com_funcionario_atribuido()
        nova_prioridade = 3

        ocorrencia_bug.mudar_prioridade(nova_prioridade)

        self.assertEqual(ocorrencia_bug.prioridade, nova_prioridade)

    def test_altera_prioridade_ocorrencia_fechada(self):
        empresa_a, jorge, projeto_1, ocorrencia_bug = self.criar_ocorrencia_com_funcionario_atribuido()
        nova_prioridade = 3
        ocorrencia_bug.fechar()

        ocorrencia_bug.mudar_prioridade(nova_prioridade)

        self.assertNotEqual(ocorrencia_bug.prioridade, nova_prioridade)

    def test_altera_funcionario_ocorrencia_fechada(self):
        empresa_a, jorge, projeto_1, ocorrencia_bug = self.criar_ocorrencia_com_funcionario_atribuido()
        pedro = Funcionario("Pedro")
        empresa_a.incluir_funcionario(pedro)
        empresa_a.incluir_funcionario_em_projeto(pedro, projeto_1)
        ocorrencia_bug.fechar()

        projeto_1.atribuir_funcionario_a_ocorrencia(pedro, ocorrencia_bug)

        self.assertNotEqual(ocorrencia_bug.funcionario, pedro)

    def test_concluir_ocorrencia_ja_fechada(self):
        empresa_a, jorge, projeto_1, ocorrencia_bug = self.criar_ocorrencia_com_funcionario_atribuido()
        ocorrencia_bug.fechar()

        with self.assertRaises(Exception):
            ocorrencia_bug.fechar()

    def test_maximo_ocorrencias_por_funcionario(self):
        empresa_a, jorge, projeto_1, ocorrencias = self.criar_dez_ocorrencias_atribuidas_ao_funcionario()
        nova_ocorrencia = projeto_1.cria_ocorrencia("Ocorrencia a mais")

        with self.assertRaises(LimiteOcorrenciasPorFuncionarioAtingidoException):
            projeto_1.atribuir_funcionario_a_ocorrencia(jorge, nova_ocorrencia)

if __name__ == '__main__':
    unittest.main()
