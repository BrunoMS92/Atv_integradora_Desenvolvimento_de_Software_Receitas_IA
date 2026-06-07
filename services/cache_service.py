import json


class CacheService:

    def ler_cache(self):

        with open("cache.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)