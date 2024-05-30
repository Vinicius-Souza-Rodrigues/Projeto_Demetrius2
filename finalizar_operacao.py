#função confusa, necessidade de sepração de funções!
def finalizar_operacao(vendedores_lista, carrinho_lista):
    preco_total = 0
    for dicionario in carrinho_lista:
        preco_total += dicionario["quantidade"] * dicionario["preco"]
        taxa_vendedor = preco_total * 0.05

        for dicionario_vendedor in vendedores_lista:
            if dicionario["codigo_vendedor"] == dicionario_vendedor["codigo_vendedor"]:
                dicionario_vendedor["lucro"] = taxa_vendedor
        #revisar abaixo
        for vendedores in vendedores_lista:
            print(f'O {vendedores["nome"]} lucrou: {vendedores["lucro"]}R$!')
    
    print(vendedores_lista)
    print(f'''O preço total arrecadado foi de {preco_total} R$!
O roubo foi de {preco_total * 0.25}R$ deixando de valor bruto em {preco_total - (preco_total * 0.25)}R$
''')
