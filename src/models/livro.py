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



    def emprestado(self, cpf_usuario, data_emprestimo): 
        if not isinstance(cpf_usuario, User_Student) or not hasattr(cpf_usuario, "cpf_usuario"):

            raise TypeError("O parâmetro 'user' deve ser uma instância de User_Student com o atributo 'id_usuario'.")


        self.cpf_usuario = cpf_usuario.cpf_usuario
        # acessando o cpf_usuario da class e declarando que ele tem um valor de (cpf_usuario.cpf_usuario) que seria 
        if not self.disponivel:
            print("ERROR: Livro já emprestado.")
            return # impossibilita emprestimo se ja estiver emprestado
        try:
            self.data_emprestimo = datetime.strptime(data_emprestimo, "%d/%m/%Y") # se as datas n estiverem no formato que deveriam
        except ValueError:
            raise ValueError("Data de empréstimo deve estar no formato dd/mm/yyyy.")

        self.disponivel = False; # livro emprestado




    def devolvido(self, data_devolucao, cpf_usuario):
        if self.data_emprestimo or cpf_usuario is None:
            print("ERROR: esse não foi o livro emprestado.")
            return # sai do metodo
        self.data_devolucao = datetime.strptime(data_devolucao, "%d/%m/%Y")
        self.maxdata_devolucao = self.data_emprestimo + timedelta(days=30)

        if self.data_devolucao > self.maxdata_devolucao and self.cpf_usuario: 
            self.user.credito_emprestimo -= 1  # reduz o credito
        self.disponivel = True; self.cpf_usuario = None; # remove a referencia do usuario ja q o livro ja foi devolvido
