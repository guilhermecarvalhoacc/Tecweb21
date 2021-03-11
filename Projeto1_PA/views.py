from utils import load_data, load_template,build_response
import urllib
import json
from database import Database, Note

database = Database("BANCO_DB")

def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        lista_post = []
        for chave_valor in corpo.split('&'):
            lista = urllib.parse.unquote_plus(chave_valor).split("=")
            print(f"ESSA AKI EH A LISTA: {lista}")
            print(f"\n\n {chave_valor}")
            lista_post.append(lista[1])
            # AQUI É COM VOCÊ
        print(f"PARAMS EH: {corpo}")
        
        database.add(Note(title= lista_post[0], content= lista_post[1]))
        return build_response(code=303, reason='See Other', headers='Location: /') 

        
    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...
    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    else:
        note_template = load_template('components/note.html')
        notes_li = [
            note_template.format(title=dados.title, details=dados.content)
            for dados in database.get_all()
        ]
        notes = '\n'.join(notes_li)

        return build_response() + load_template('index.html').format(notes=notes).encode()
