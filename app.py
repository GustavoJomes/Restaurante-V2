import os
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('mexican food', 'mexicana')
restaurante_japones = Restaurante('japa', 'japonesa')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)


def main():
    os.system('cls')
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
