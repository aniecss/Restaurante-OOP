from restaurante import Restaurante

def main():
    restaurante1 = Restaurante('Praça', 'Gourmet')
    restaurante1.receber_avaliacao('Ana', 5)
    restaurante1.receber_avaliacao('Maria', 4)
    restaurante1.receber_avaliacao('Júlia', 3)

    print('\n--- Lista de Restaurantes ---\n')
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
    