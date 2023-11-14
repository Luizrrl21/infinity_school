frase = ["Python", "é", "uma", "linguagem", "poderosa"]
new = []

for i in frase:
    if len(i) > 4:
        new.append(i)

print(f"{new[0]} - {new[1]} - {new[2]}")