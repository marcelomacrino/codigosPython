listaCompras = ["Arroz","Feijao"]

novoProduto = input("Digite um novo produto na lista: ")

listaCompras.append(novoProduto)

if "Chocolate" in listaCompras:
    print("Não esqueça da sobremesa")

print(listaCompras)