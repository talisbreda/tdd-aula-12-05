class Ocorrencia:
    funcionario = None

    def __init__(self, nome):
        self.nome = nome

    def atribuir_funcionario(self, funcionario):
        self.funcionario = funcionario