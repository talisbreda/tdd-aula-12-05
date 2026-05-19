class Ocorrencia:
    id = 0

    def __init__(self, nome):
        self.nome = nome
        self.funcionario = None
        self.id = self.incrementa_contador()
        self.estado = 'ABERTO'

    def incrementa_contador(contador):
        Ocorrencia.id += 1
        return Ocorrencia.id

    def atribuir_funcionario(self, funcionario):
        self.funcionario = funcionario

from enum import Enum

class EstadoEnum(Enum):
    ABERTO = 'ABERTO',
    FECHADO = 'FECHADO'