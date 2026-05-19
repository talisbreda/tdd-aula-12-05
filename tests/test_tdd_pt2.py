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
    
    def criar_empresa(self):
        nome = "Empresa A"
        empresa = Empresa(nome)
        return empresa

    # Criação de ocorrencia
    def test_cria_ocorrência(self):
        empresa, funcionario, projeto = self.criar_objetos_incluindo_funcionario_em_projeto()

        ocorrencia = projeto.cria_ocorrencia("bugTeste")

        self.assertTrue( ocorrencia in projeto.ocorrencias)
    
    

if __name__ == '__main__':
    unittest.main()
