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
        self.funcionario = funcionario

    def fechar(self):
        self.estado = EstadoEnum.FECHADO

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