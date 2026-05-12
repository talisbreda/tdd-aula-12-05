class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def incluir_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)