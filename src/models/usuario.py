class User_Student:
    def __init__(self, nome, id_usuario, credito_emprestimo = 60):
        self.nome = nome
        self.id_usuario = id_usuario
        self.credito_acesso = True
        self.credito_emprestimo = credito_emprestimo; 
    # inicialmente pode ter acesso aos livros (60 credito)
