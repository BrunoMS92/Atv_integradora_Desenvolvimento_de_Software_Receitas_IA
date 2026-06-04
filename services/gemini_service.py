import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class GeminiService:

    def gerar_receita(self, pedido):

        model = genai.GenerativeModel("gemini-2.5-flash")

        resposta = model.generate_content(
            f"Crie uma receita completa de {pedido}"
        )

        return resposta.text