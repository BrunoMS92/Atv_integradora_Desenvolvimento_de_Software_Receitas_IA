from views.menu import pedir_receita
from controllers.receita_controller import ReceitaController


def main():

    pedido = pedir_receita()

    controller = ReceitaController()

    receita = controller.criar_receita(pedido)

    print("\nReceita gerada:\n")
    print(receita.conteudo)


if __name__ == "__main__":
    main()