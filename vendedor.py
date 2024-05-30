#cadastro de venedor e verificação do vendedor!
def cadastrar_vendedor(vendedores_lista):
    while True:
        vendedor = {
            "nome": str(input('Digite o seu nome!: ')),
            "codigo_vendedor": int(input('Digite o seu codigo de vendedor!: ')),
            "lucro": 0
        }

        for dicionario in vendedores_lista:
            if dicionario["codigo_vendedor"] == vendedor["codigo_vendedor"]:
                print(f'O codigo de vendedor {vendedor["codigo_vendedor"]} já está em uso!')
                return
        
        vendedores_lista.append(vendedor)
        print(f'O vendedor foi cadastrado com sucesso!')
        outro_vendedor = str(input('Deseja adicionar outro vendedor! [Y/N]: ').upper())
        if outro_vendedor == 'N':
            break
