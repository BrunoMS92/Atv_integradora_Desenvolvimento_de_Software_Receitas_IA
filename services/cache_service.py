import json


class CacheService:

    def ler_cache(self):

        with open("cache.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        
    def salvar_cache(self, pedido):

        receitas = self.ler_cache()

        receitas.append(
            {
                "pedido": pedido
            }
        )

        receitas = receitas[-5:]

        with open("cache.json", "w", encoding="utf-8") as arquivo:
            json.dump(receitas, arquivo, indent=4, ensure_ascii=False)