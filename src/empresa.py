class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def incluir_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def incluir_projeto(self, projeto):
        self.projetos.append(projeto)