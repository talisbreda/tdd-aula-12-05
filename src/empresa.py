class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def incluir_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def incluir_projeto(self, projeto):
        self.projetos.append(projeto)
    
    def incluir_funcionario_em_projeto(self, funcionario, projeto):
        if funcionario in self.funcionarios and projeto in self.projetos:
            projeto.incluir_funcionario(funcionario)