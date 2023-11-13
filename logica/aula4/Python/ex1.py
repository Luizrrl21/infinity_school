while True:
    nota = int(input("Digite a nota do Aluno: "))
    if nota > 10 or nota < 0:
        print(f"{nota} não é uma nota válida, Digite um número de 0 a 10")
    else:
        print("Nota do aluno foi registrada!")
        break
    