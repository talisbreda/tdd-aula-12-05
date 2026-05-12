class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def incluir_funcionario(self, funcionario):
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)