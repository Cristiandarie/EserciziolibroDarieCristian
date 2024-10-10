class Libro:
    def __init__(self, titolo, anno, autore):
        self.titolo = titolo
        self.anno = anno
        self.autore = autore
    def get_titolo(self):
        return self.titolo
    def get_anno(self):
        return self.anno
    def get_autore(self):
        return self.autore
    def set_titolo(self, titolo):
        self.titolo = titolo
    def set_anno(self, anno):
        self.anno = anno
    def set_autore(self, autore):
        self.autore = autore
    def _toString_(self):
        return f"Libro: '{self.titolo}', Anno: {self.anno}, Autore: {self.autore}"

def inserisci_libro():
        titolo = input("Inserisci il titolo del libro:")
        anno = input("Inserisci l'anno di pubblicazione:")
        autore = input("Inserisci il nome dell'autore:")
        libro = (titolo, anno, autore)
        return libro
libro_utente = inserisci_libro()
print(libro_utente)