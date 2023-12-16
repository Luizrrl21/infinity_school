import re

def v_nome(nome):
    # Expressão regular para verificar se é um nome válido
    padrao_nome = re.compile(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$')

    if padrao_nome.match(nome):
        return True
    else:
        print("Erro: Nome inválido.")
        return False

def v_cpf(cpf):
    # Expressão regular para validar CPF
    padrao_cpf = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

    if padrao_cpf.match(cpf):
        numeros_cpf = re.sub(r'[^\d]', '', cpf)

        if not all(num == numeros_cpf[0] for num in numeros_cpf):
            digitos_verificadores = numeros_cpf[-2:]

            soma = sum(int(num) * peso for num, peso in zip(numeros_cpf[:9], range(10, 1, -1)))
            resto = soma % 11
            digito1 = 11 - resto if resto > 1 else 0

            soma = sum(int(num) * peso for num, peso in zip(numeros_cpf[:10], range(11, 1, -1)))
            resto = soma % 11
            digito2 = 11 - resto if resto > 1 else 0

            if digito1 == int(digitos_verificadores[0]) and digito2 == int(digitos_verificadores[1]):
                return True

    print("Erro: CPF inválido.")
    return False

def v_valor(valor):
    # Expressão regular para verificar se é um valor válido em reais
    padrao_valor = re.compile(r'^[1-9]\d{0,2}(\.\d{3})*,\d{2}$')

    if padrao_valor.match(valor):
        return True
    else:
        print("Erro: Valor em reais inválido.")
        return False

