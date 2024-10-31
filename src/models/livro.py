from datetime import datetime, timedelta
from models.usuario import User_Student

class Book:
    def __init__ (self, titulo, autor, ano, id_livro):
        self.titulo = titulo
        self.autor = autor
        self.id_livro = id_livro
        self.ano = ano
        self.disponivel = True
        self.user = None
        self.data_emprestimo = None 
        self.data_devolucao = None # Achei interessante ter esse atributo para colocar na tabela.
        # inicialmente no sistema o livro nao foi emprestado (sem user), nao apresentando data de emprestimo (ele vai ganhando um historico de data de emprestimos)        

    def emprestado(self, user, data_emprestimo): 
        if not isinstance(user, User_Student) or not hasattr(user, "id_usuario"):
            raise TypeError("O parâmetro 'user' deve ser uma instância de User_Student com o atributo 'id_usuario'.")
        self.user_id = user.id_usuario
        self.user = user 
        if not self.disponivel:
            print("ERROR: Livro já emprestado.")
            return # impossibilita emprestimo se ja estiver emprestado
        self.data_emprestimo = datetime.strptime(data_emprestimo, "%d/%m/%Y");
        self.disponivel = False; # livro emprestado

    def devolvido(self, data_devolucao):
        if self.data_emprestimo is None:
            print("ERROR: esse não foi o livro emprestado.")
            return
        self.data_devolucao = datetime.strptime(data_devolucao, "%d/%m/%Y")
        self.maxdata_devolucao = self.data_emprestimo + timedelta(days=30)

        if self.data_devolucao > self.maxdata_devolucao and self.user: 
            self.user.credito_emprestimo -= 1  # reduz o credito
        self.disponivel = True; self.user = None; # remove a referencia do usuario ja q o livro ja foi devolvido
