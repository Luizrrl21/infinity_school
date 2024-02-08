class Project:
    def __init__(self, project:str, deadline:str):
        self.__project = project
        self.__entrega = deadline

class Task(Project):
    def __init__(self, project: str, deadline: str, tarefa: str, responsible: str, stats):
        super().__init__(project, deadline)
        self.__tarefa = tarefa
        self.__responsible = responsible
        self.__stats = stats

while True:
    acao = str(input("Qual opção você deseja fazer"))

