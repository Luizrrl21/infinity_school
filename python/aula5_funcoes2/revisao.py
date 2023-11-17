def maior(a:int, b:int) -> str:
    if a > b:
        return f"O {a} é maior que o {b}"
    elif b > a:
        return f"O {b} é maior que o {a}"
    else:
        return f"Os números são iguais"
    
print(maior(50, 50))