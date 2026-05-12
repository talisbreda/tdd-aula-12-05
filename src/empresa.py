class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.projetos = []

    def incluir_funcionario(self, funcionario):
        if funcionario not in self.funcionarios:
            self.funcionarios.append(funcionario)

    def incluir_funcionarios(self, funcionarios):
        for f in funcionarios:
            self.incluir_funcionario(f)

    def incluir_projeto(self, projeto):
        if projeto not in self.projetos:
            self.projetos.append(projeto)

    def incluir_projetos(self, projetos):
        for p in projetos:
            self.incluir_projeto(p)
    
    def incluir_funcionario_em_projeto(self, funcionario, projeto):
        if funcionario in self.funcionarios and projeto in self.projetos:
            projeto.incluir_funcionario(funcionario)

    def incluir_funcionario_em_projetos(self, funcionario, projetos):
        for p in projetos:
            self.incluir_funcionario_em_projeto(funcionario, p) 
