from utils import load_data, load_template,build_response
import urllib
import json
from database import Database 


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            lista = urllib.parse.unquote_plus(chave_valor).split("=")
            params[lista[0]] = lista[1]
            print(f"\n\n {chave_valor}")
            # AQUI É COM VOCÊ
            
        database = Database("BANCO_DB")
        db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
        db.add(Note(title=None, content='Lembrar de tomar água'))

'''        with open("data/notes.json") as arq_note:
            data = json.load(arq_note)
        data.append(params)
        with open("data/notes.json", "w") as f:
            json.dump(data,f) #para escrever o novo dicionario no arquivo json'''

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
