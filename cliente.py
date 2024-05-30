cliente_lista = []

def cadastrar_cliente(cliente_lista):
    while True:
        cliente = {
            "nome": str(input('Digite o seu nome!: ')),
            "CPF": int(input('Digite o seu CPF!: ')),
            "Telefone": int(input('Digite o seu número de telefone!: '))
        }

        for dicionario in cliente_lista:
            if dicionario["CPF"] == cliente["CPF"]:
                print(f'O CPF {cliente["CPF"]} já está em uso!')
                return
            
        cliente_lista.append(cliente)
        print(f'O cliente {cliente["nome"]} foi cadastrado com sucesso!')
        outro_cliente = str(input('Gostaria de adicionar outro cliente! [Y/N]: ').upper())
        if outro_cliente == 'N':
            break
