from models.livro import *
from models.usuario import *
from services.persistencia import *
import os

# Só Para Testes

def criar_pasta_data():
    if not os.path.exists('./data'):
        os.makedirs('./data')

criar_pasta_data()

with open('./data/books.db', 'w') as f:
    pass

with open('./data/users.db', 'w') as f:
    pass