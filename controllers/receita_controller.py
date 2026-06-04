from models.receita import Receita
from services.gemini_service import GeminiService


class ReceitaController:

    def criar_receita(self, pedido):

        service = GeminiService()

        conteudo = service.gerar_receita(pedido)

        return Receita(conteudo)