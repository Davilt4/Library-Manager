# user id = cpf -> ate poderia ser um id gerado, mas por agora fica mais simples com o proprio user cpf
class User_Student:
    def __init__(self, nome, cpf_usuario, credito_emprestimo = 60):
        self.nome = nome
        self.cpf_usuario = cpf_usuario
        self.credito_acesso = True
        self.credito_emprestimo = credito_emprestimo; 
    # inicialmente pode ter acesso aos livros (60 credito)
