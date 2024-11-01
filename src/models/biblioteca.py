# IMPORTING MODULES
from datetime import datetime, timedelta; # -> formato data tipo (dd/mm/aaaa): so aceita esse formato, util p contagem de dias
from models.usuario import User_Student
from models.livro import Book
import uuid; # -> codigo do emprestimo (36 caract. aleatorios) -> interessante p registro

'''
HASATTR : verifica se um objeto possui um determinado < atributo >
ISINSTACE :  usada para verificar se um objeto < é uma instância de uma determinada classe >
'''
class Library:
    def emprestado(self, instance_user_id, instance_disponivel, data_emprestimo, ): 
        # SE USER_ID NÃO É UMA INSTANCIA DE USER_STUDENT (OU) NÃO TEM O ATRIBUTO USER_ID
        if not isinstance(instance_user_id, User_Student) or not hasattr(instance_user_id, "user_id"):
            raise TypeError("O parâmetro 'user' deve ser uma instância de User_Student com o atributo 'user_id'.")

                        #(a)    (b)
        self.user_id = instance_user_id.user_id # o 'user_id' dentro do objeto User_Student é copiado para a Library -> preciso estudar isso melhor
#         (a)  objeto de User_Student (parâmetro do método).
#         (b) atributo user_id dentro dessa instância de User_Student, que contém o ID real do usuário (como uma string ou outro identificador).
        if not isinstance(instance_disponivel, Book) or not hasattr(instance_disponivel, "disponivel"):
            raise TypeError("O parâmetro 'disponivel' deve ser uma instância de Book com o atributo 'disponivel'.")
        
        if not self.Book.disponivel:
            print("ERROR: Livro já emprestado.")
            return # impossibilita emprestimo se ja estiver emprestado
        try:
            self.data_emprestimo = datetime.strptime(data_emprestimo, "%d/%m/%Y") 
            # se as datas n estiverem no formato que deveriam
        #   ------------------------------------------------------> GERAR CODIGO DO EMPRESTIMO AQUI
        except ValueError:
            raise ValueError("Data de empréstimo deve estar no formato dd/mm/yyyy.")

        self.disponivel = False; # livro emprestado


    def devolvido(self, data_devolucao, user_id):
        if self.data_emprestimo or user_id is None:
            print("ERROR: esse não foi o livro emprestado.")
            return # sai do metodo
        self.data_devolucao = datetime.strptime(data_devolucao, "%d/%m/%Y")
        self.maxdata_devolucao = self.data_emprestimo + timedelta(days=30)

        if self.data_devolucao > self.maxdata_devolucao and self.user_id: 
            self.user.credito_emprestimo -= 1  # reduz o credito
        self.disponivel = True; self.user_id = None; # remove a referencia do usuario ja q o livro ja foi devolvido