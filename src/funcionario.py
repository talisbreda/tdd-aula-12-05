class Funcionario:

    def __init__(self, nome):
        self.nome = nome
        self.ocorrencias = []

    def adicionar_em_ocorrencia(self, ocorrencia):
        if ocorrencia not in self.ocorrencias:
            self.ocorrencias.append(ocorrencia)
    
    def remover_de_ocorrencia(self, ocorrencia):
        self.ocorrencias.remove(ocorrencia)