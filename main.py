from services.gemini_service import GeminiService


def main():

    service = GeminiService()

    resposta = service.gerar_receita("Lasanha de frango")

    print(resposta)


if __name__ == "__main__":
    main()