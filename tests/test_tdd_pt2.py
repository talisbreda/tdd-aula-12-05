import sys
import os
_d = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _d)
sys.path.insert(0, os.path.join(os.path.dirname(_d), 'src'))

from empresa import Empresa
from funcionario import Funcionario
from projeto import Projeto
from ocorrencia import Ocorrencia, EstadoEnum
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
    
    def criar_objetos_incluindo_funcionario_em_projeto(self):
        nome = "Empresa A"
        empresa = Empresa(nome)
        nome_funcionario = "Jorge"
        funcionario = Funcionario(nome_funcionario)
        nome_projeto = "Projeto 1"
        projeto = Projeto(nome_projeto)
        empresa.incluir_funcionario(funcionario)
        empresa.incluir_projeto(projeto)
        empresa.incluir_funcionario_em_projeto(funcionario, projeto)

        return empresa, funcionario, projeto
    
    def criar_objetos_ocorrencia(self):
        nome = "Empresa A"
        empresa = Empresa(nome)
        nome_funcionario = "Jorge"
        funcionario = Funcionario(nome_funcionario)
        nome_projeto = "Projeto 1"
        projeto = Projeto(nome_projeto)
        empresa.incluir_funcionario(funcionario)
        empresa.incluir_projeto(projeto)
        empresa.incluir_funcionario_em_projeto(funcionario, projeto)
        ocorrencia = projeto.cria_ocorrencia("bugTeste")
        projeto.atribuir_funcionario_a_ocorrencia(funcionario, ocorrencia)

        return empresa, funcionario, projeto, ocorrencia
    
    
    def criar_empresa(self):
        nome = "Empresa A"
        empresa = Empresa(nome)
        return empresa

    # Criação de ocorrencia
    def test_cria_ocorrencia(self):
        empresa, funcionario, projeto = self.criar_objetos_incluindo_funcionario_em_projeto()

        ocorrencia = projeto.cria_ocorrencia("bugTeste")

        self.assertTrue( ocorrencia in projeto.ocorrencias)
    
    
    # Atribui funcionario a ocorrência
    def test_atribui_funcionario_ocorrencia(self):
        empresa, funcionario, projeto = self.criar_objetos_incluindo_funcionario_em_projeto()
        ocorrencia = projeto.cria_ocorrencia("bugTeste")

        ocorrencia.atribuir_funcionario(funcionario)

        self.assertEqual(ocorrencia.funcionario, funcionario)

    def test_atribui_funcionario_fora_do_projeto_em_ocorrencia(self):
        empresa, funcionario, projeto = self.criar_objetos()
        ocorrencia = projeto.cria_ocorrencia("bugTeste")

        projeto.atribuir_funcionario_a_ocorrencia(funcionario, ocorrencia)

        self.assertNotEqual(ocorrencia.funcionario, funcionario)

    def test_ultimo_funcionario_ocorrencia(self):
        empresa, funcionario, projeto = self.criar_objetos_incluindo_funcionario_em_projeto()
        funcionarioPedro = Funcionario("Pedro")
        empresa.incluir_funcionario(funcionarioPedro)
        projeto.incluir_funcionario(funcionarioPedro)
        ocorrencia = projeto.cria_ocorrencia("bugTeste")
        ocorrencia.atribuir_funcionario(funcionario)
        
        ocorrencia.atribuir_funcionario(funcionarioPedro)

        self.assertEqual(ocorrencia.funcionario, funcionarioPedro)

    def test_identificador_unico(self):
        empresa, funcionario, projeto = self.criar_objetos()
        ocorrenciaBug = projeto.cria_ocorrencia("bugTeste")
        ocorrenciaTarefa = projeto.cria_ocorrencia("bugTeste")

        self.assertNotEqual(ocorrenciaBug.id, ocorrenciaTarefa.id)

    def test_ocorrencia_aberta(self):
        empresa, funcionario, projeto, ocorrencia = self.criar_objetos_ocorrencia()

        self.assertTrue(ocorrencia.estado == EstadoEnum.ABERTO)

    def test_concluir_ocorrencia(self):
        empresa, funcionario, projeto, ocorrencia = self.criar_objetos_ocorrencia()

        ocorrencia.fechar()

        self.assertTrue(ocorrencia.estado == EstadoEnum.FECHADO)

    def test_altera_prioridade_ocorrencia_aberta(self):
        empresa, funcionario, projeto, ocorrencia = self.criar_objetos_ocorrencia()
        nova_prioridade = 3

        ocorrencia.mudar_prioridade(nova_prioridade)

        self.assertEqual(ocorrencia.prioridade, nova_prioridade)

    def test_altera_prioridade_ocorrencia_fechada(self):
        empresa, funcionario, projeto, ocorrencia = self.criar_objetos_ocorrencia()
        nova_prioridade = 3
        ocorrencia.fechar()

        ocorrencia.mudar_prioridade(nova_prioridade)

        self.assertNotEqual(ocorrencia.prioridade, nova_prioridade)

    def test_altera_funcionario_ocorrencia_fechada(self):
        empresa, funcionario, projeto, ocorrencia = self.criar_objetos_ocorrencia()
        funcionarioPedro = Funcionario("Pedro")
        empresa.incluir_funcionario(funcionarioPedro)
        empresa.incluir_funcionario_em_projeto(funcionarioPedro, projeto)
        ocorrencia.fechar()

        projeto.atribuir_funcionario_a_ocorrencia(funcionarioPedro, ocorrencia)

        self.assertNotEqual(ocorrencia.funcionario, funcionarioPedro)

    def test_concluir_ocorrencia_ja_fechada(self):
        empresa, funcionario, projeto, ocorrencia = self.criar_objetos_ocorrencia()
        ocorrencia.fechar()

        with self.assertRaises(Exception):
            ocorrencia.fechar()


if __name__ == '__main__':
    unittest.main()
