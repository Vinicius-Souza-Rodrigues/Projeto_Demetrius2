import produto
import cliente
import carrinho
import vendedor
import finalizar_operacao

produtos_lista = []
carrinho_lista = []
vendedores_lista = []
clientes_lista = []

while True:
      print('-=' * 20)
      print('''Tabela de Opções!
      [1] Cadastrar Produto!
      [2] Cadastrar Cliente!
      [3] Cadastrar Vendedor!
      [4] Relátorio de Vendas!
      [5] Carrinho!
      [6] Finalizar Compra!''')
      print('=-' * 20)

      opcao = input('Digite qual a ordem!: ')

      if opcao == '1':
            produto.cadastrar_produto(produtos_lista)
      elif opcao == '2':
            cliente.cadastrar_cliente(clientes_lista)
      elif opcao == '3':
            vendedor.cadastrar_vendedor(vendedores_lista)
      elif opcao == '4':
            finalizar_operacao.finalizar_operacao(vendedores_lista, carrinho_lista)
      elif opcao == '5':
            carrinho.menu_carrinho(produtos_lista, carrinho_lista, vendedores_lista)
      elif opcao == '6':
            print(f'Finalizar ações!')
            finalizar_operacao.finalizar_operacao(vendedores_lista, carrinho_lista)
            break
      else:
            print(f'Digite uma ação válida!')
