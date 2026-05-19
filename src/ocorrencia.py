class Ocorrencia:
    id = 0

    def __init__(self, nome):
        self.nome = nome
        self.funcionario = None
        self.id = self.incrementa_contador()
        self.estado = EstadoEnum.ABERTO
        self.resumo = ""
        self.prioridade = PrioridadeEnum.BAIXA

    def incrementa_contador(contador):
        Ocorrencia.id += 1
        return Ocorrencia.id

    def atribuir_funcionario(self, funcionario):
        if self.estado == EstadoEnum.ABERTO:
            self.funcionario = funcionario

    def fechar(self):
        if self.estado == EstadoEnum.FECHADO:
            raise Exception("Ocorrência já fechada")
        self.estado = EstadoEnum.FECHADO
        self.funcionario.remover_de_ocorrencia(self)
        

    def mudar_prioridade(self, prioridade):
        if prioridade in PrioridadeEnum and self.estado == EstadoEnum.ABERTO:
            self.prioridade = prioridade

from enum import Enum

class EstadoEnum(Enum):
    ABERTO = 'ABERTO',
    FECHADO = 'FECHADO'

class PrioridadeEnum(Enum):
    ALTA = 3
    MEDIA = 2
    BAIXA = 1

class LimiteOcorrenciasPorFuncionarioAtingidoException(Exception):
    pass