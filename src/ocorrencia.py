class Ocorrencia:
    id = 0

    def __init__(self, nome):
        self.nome = nome
        self.funcionario = None
        self.id = self.incrementa_contador()
        self.estado = EstadoEnum.ABERTO

    def incrementa_contador(contador):
        Ocorrencia.id += 1
        return Ocorrencia.id

    def atribuir_funcionario(self, funcionario):
        self.funcionario = funcionario

    def fechar(self):
        self.estado = EstadoEnum.FECHADO

from enum import Enum

class EstadoEnum(Enum):
    ABERTO = 'ABERTO',
    FECHADO = 'FECHADO'