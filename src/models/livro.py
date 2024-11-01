class Book:
    # estado inicial do livro -> (da instancia) quando chama a class
    def __init__ (self, titulo, autor, ano, id_livro):
        self.titulo = titulo
        self.autor = autor
        self.id_livro = id_livro
        self.ano = ano
        self.disponivel = True
        self.user = None
        self.data_emprestimo = None 
        self.data_devolucao = None