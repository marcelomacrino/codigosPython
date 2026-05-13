alunosProva = int(input("Digite o numero de alunos que fizeram a prova: "))
nota = []
numero = 0
somaGeral = 0
mediaGeral = 0

while numero < alunosProva:
    notas = float(input(f"Digite a nota do aluno {numero+1}: "))
    nota.append(notas)
    somaGeral += nota[numero]
    numero += 1

mediaGeral = somaGeral / numero

if mediaGeral >= 6:
    print("Turma Aprovada")
else:
    print("Turma em Recuperação")

print(f"A Media final da Turma: {mediaGeral:.2f}")




