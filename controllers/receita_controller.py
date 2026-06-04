from models.receita import Receita


class ReceitaController:

    def criar_receita(self, conteudo):

        return Receita(conteudo)