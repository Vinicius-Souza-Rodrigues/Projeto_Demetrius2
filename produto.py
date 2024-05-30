#cadastro de produtos, aumento de estoque e verificação do produto
def cadastrar_produto(produtos_lista):
    while True:
        produto = {
            "nome": input('Digite o nome do produto!: '),
            "codigo_produto": int(input('Digite o codigo do produto!: ')),
            "preco": float(input('Digite o preço do produto!: ')),
            "quantidade": int(input('Digite a quantidade que gostaria de adicionar!: '))
        }

        for dicionario in produtos_lista:
            if dicionario["codigo_produto"] == produto["codigo_produto"]:
                print(f'O produto {produto["nome"]} já foi cadastrado com o codigo {produto["codigo_produto"]}!')
                if dicionario["nome"] == produto["nome"]:
                    estoque = str(input('Gostaria de aumentar o estoque!: ').upper())
                    if estoque == 'Y':
                        dicionario["quantidade"] += produto["quantidade"]
                return

        produtos_lista.append(produto)
        print(f'Produto cadastrado com sucesso!')
        outro_produto = str(input('Deseja adicionar outro produto!: [Y/N]!: ').upper())
        if outro_produto == 'N':
            break