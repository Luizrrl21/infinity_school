n1 = float(input("Digite a nota da prova 1: "))
n2 = float(input("Digite a nota da prova 2: "))
media = (n1+n2)/2

if media == 10:
    print(f"Aluno aprovado com distinção! (Média = {media})")
elif media >= 7:
    print(f"Aluno aprovado! (Média = {media})")
else:
    print(f"Aluno reprovado! (Média = {media})")