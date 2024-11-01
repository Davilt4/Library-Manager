# IMPORTING MODULES
import secrets # -> para criar um user_id

# entrada: NOME & CPF e '''se ja tiver cadastro o id_user'''
class User_Student:
    def __init__(self, nome, cpf, credito_emprestimo=60, user_id=None):
        self.nome = nome
        self.cpf = cpf
        # if um user_id for fornecido, ele será usado -> else, será gerado um novo
        self.user_id = user_id if user_id else f"user_{secrets.token_hex(4)}" # if-else compacto nunca tinha visto gostei e coloquei
        # instancia user.id = igual a instancia SE True, se nao (None entraria como False) e geraria outro ID
        self.credito_acesso = True # consequencia do credito de emprestimo
        self.credito_emprestimo = credito_emprestimo # = 60
# pedi p chat gpt fazer um teste:
'''
    def __str__(self):
        return (f"User ID: {self.user_id}\n"
                f"Nome: {self.nome}\n"
                f"CPF: {self.cpf}\n"
                f"Crédito para Empréstimo: {self.credito_emprestimo}\n"
                f"Acesso: {'Sim' if self.credito_acesso else 'Não'}\n")


# Exemplo de uso
# Criando um novo usuário
novo_usuario = User_Student("Alice", "12345678900")

# Usuário existente fazendo login (com seu próprio user_id)
usuario_existente = User_Student("Bob", "09876543211", user_id="user_abcd1234")

print(novo_usuario)
print(usuario_existente)
'''

