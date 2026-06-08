from controllers.receita_controller import ReceitaController
from models.receita import Receita


def test_controller_retorna_objeto_receita(monkeypatch):

    class GeminiFake:

        def gerar_receita(self, pedido):
            return "Receita para testar"

    monkeypatch.setattr(
        "controllers.receita_controller.GeminiService",
        GeminiFake
    )

    # Usei o monkeypatch para não gastar minha cota da API
    controller = ReceitaController()

    resultado = controller.criar_receita("Bolo de cenoura")

    assert isinstance(resultado, Receita)