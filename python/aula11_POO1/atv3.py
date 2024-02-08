#Incompleto
class Funcionarios:
    def __init__(self, name:str , role:str, wage:float):
        self.nome = name
        self.cargo = role
        self.salario = wage

class Empresa:
    def __init__(self):
        self.lista_de_funcionarios = []

    def add_funcionario(self):
        nome_funcionario = str(input("Digite o nome do funcionário: "))
        cargo_funcionario = str(input("Digite o cargo do funcionário: "))
        salario_funcionario = float(input("Digite o salario do funcionário: "))

        funcionario = Funcionarios(name=nome_funcionario, role=cargo_funcionario, wage=salario_funcionario)
        self.lista_de_funcionarios.append(funcionario)

    def del_funcionario(self):
        nome_removido = str(input("Digite o nome do funcionário que você quer deletar: "))
        for funcionario in self.lista_de_funcionarios:
            if funcionario == nome_removido:
                self.lista_de_funcionarios.remove(nome_removido)

    def lista_de_funcionarios(self):
        for funcionario in self.lista_de_funcionarios:
            print(f"""
            Nome: {funcionario.nome}
            Cargo: {funcionario.cargo}
            Salário: {funcionario.salario}
""")
            
empresa1 = Empresa()

while True:
    menu = int(input("""
                     Escolha uma opção:
                     1 - Adicionar"""))
