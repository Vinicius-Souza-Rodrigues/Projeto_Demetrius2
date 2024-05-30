def menu_carrinho(produto_lista, carrinho_lista, vendedores_lista):
    print('''Escolha a opção do carrinho!
          [1] Adicionar produtos ao carrinho!
          [2] Remover produto ao carrinho!
          [3] Voltar/Sair
          ''') 
    opcao = input('Digite a opção deseja!:  ')

    if opcao == '1':
        adicionar_produto_carrinho(produto_lista, carrinho_lista, vendedores_lista)
    elif opcao == '2':
        remover_produto_carrinho(produto_lista, carrinho_lista)
    elif opcao == '3':
        return
    else:
        print(f'Digite uma opção válida!')

def adicionar_produto_carrinho(produto_lista, carrinho_lista, vendedores_lista):
    while True:
        carrinho_produto = {
            "nome": input('Qual o nome do produto que você deseja!: '),
            "quantidade": int(input('Qual a quantidade que você deseja!: ')),
        }

        for dicionario in produto_lista:
            if dicionario["nome"] == carrinho_produto["nome"] and dicionario["quantidade"] >= carrinho_produto["quantidade"]:
                carrinho_produto["preco"] = dicionario["preco"] #ta passando o preco
                qual_vendedor = input('Qual o nome do seu vendedor!: ')
                for dicionario_vendedor in vendedores_lista:
                    if qual_vendedor == dicionario_vendedor["nome"]:
                        carrinho_produto["codigo_vendedor"] = dicionario_vendedor["codigo_vendedor"]
                        
                dicionario["quantidade"] -= carrinho_produto["quantidade"] #ta diminuindo quantidade

                print(f'Você comprou com sucesso {carrinho_produto["quantidade"]}X de {carrinho_produto["nome"]}')
                carrinho_lista.append(carrinho_produto)
        
        outro_produto = input('Deseja adicionar outro produto ao carrinho!: [Y/N]').upper()
        if outro_produto == 'N':
            break
            
#revisar
def remover_produto_carrinho(produto_lista, carrinho_lista):
    while True:
        produto_remove = input('Qual produto você gostaria de remover!: ')
        for dicionario in carrinho_lista:
            if dicionario["nome"] == produto_remove:
                #talvez colocar essa parte com a de subtrair de "adicionar_produto_carrinho" em uma função
                for dicionario_alterado in produto_lista:
                    if dicionario_alterado["nome"] == produto_remove:
                        dicionario_alterado["quantidade"] += dicionario["quantidade"]
                        #a parte de for dicionario_alterado in produto_lista:
                carrinho_lista.remove(dicionario)
                print(f'O item foi retirado do carrinho!')

        remover_outro_produto = input('Deseja remover outro produto! [Y/N]:').upper()
        if remover_outro_produto == 'N':
            break
