from funcionario import Funcionario
from ocorrencia import Ocorrencia, LimiteOcorrenciasPorFuncionarioAtingidoException

class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.ocorrencias = []

    def incluir_funcionario(self, funcionario):
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)

    def cria_ocorrencia(self, nomeOcorrencia):
        ocorrencia = Ocorrencia(nomeOcorrencia)

        self.ocorrencias.append(ocorrencia)

        return ocorrencia
    
    def atribuir_funcionario_a_ocorrencia(self, funcionario: Funcionario, ocorrencia: Ocorrencia):
        if funcionario in self.funcionarios:
            if len(funcionario.ocorrencias) == 10:
                raise LimiteOcorrenciasPorFuncionarioAtingidoException
            ocorrencia.atribuir_funcionario(funcionario)
            funcionario.adicionar_em_ocorrencia(ocorrencia)