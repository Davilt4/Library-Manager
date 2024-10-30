from datetime import datetime, timedelta
from models.usuario import *
'''
para consertar irei me apegar ao cpf do usuario, de toda forma havera uma tabela com nome - cpf etc e o programa reconhecera o nome de quem pegou o livro -> vou fazer a ativ de protocolos e ja arrumo.

'''
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

    # user == instancia da class User_Student -> precisa de uma garantia melhor d/que vem da User_Student
    def emprestado(self, user, data_emprestimo): 
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
