import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self,BANCO_DB):
        self.conn = sqlite3.connect(BANCO_DB + ".db")
        self.conn.execute('''CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING , content STRING NOT NULL);''')

    def add(self,note):
        adicionando = "INSERT INTO note (title,content) VALUES ('{}','{}');".format(note.title,note.content)
        self.conn.execute(adicionando)
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute("SELECT id,title,content FROM note")
        lista = []
        for linha in cursor:
            lista.append(Note(linha[0],linha[1],linha[2]))
        return lista

    def update(self, entry):
        self.conn.execute(f"UPDATE note SET title = '{entry.title}', content = '{entry.content}' WHERE id = {entry.id}")
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute(f"DELETE FROM note WHERE id = {note_id}")
        self.conn.commit()