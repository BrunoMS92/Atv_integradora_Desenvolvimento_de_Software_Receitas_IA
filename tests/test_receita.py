from models.receita import Receita


def test_criar_receita():

    receita = Receita("Bolo de cenoura")

    assert receita.conteudo == "Bolo de cenoura"