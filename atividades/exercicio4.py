listaEstoque  = []
opcao = 0

while opcao != 3:
    print("1 - Adicionar um produto a lista")
    print("2 - Remover um produto da lista(Pelo Nome)")
    print("3 - Sair do Programa")
    opcao = int(input("Digite uma opção: "))
    if opcao == 1:
        produto = input("Digite o nome do produto: ")
        if produto in listaEstoque:
            print("Produto já está na lista")
        else:
            listaEstoque.append(produto)
            print("Produto adicionado com sucesso")
    else:
        if opcao == 2:
            produto = input("Digite o nome do produto que deseja remover: ")
            if produto in listaEstoque:
                listaEstoque.remove(produto)
                print("Produto removido com sucesso")
            else:
                print("Produto não encontrado na lista")
    print(f"Lista de Produtos Atualizada: {listaEstoque}")
print("Programa Finalizado")

            
