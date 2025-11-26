class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def is_adult(self):
        return self.eta > 18
    
persona = Persona("Ciao",22)
print(persona.is_adult())

class Registro:
    def __init__(self):
        self.studenti = []

    def addStudente(self,studente):
        self.studenti.append(studente)
        return True

    def media_voti(self,studente):
        sum = 0
        for voto in studente.voti.values():
            sum += voto
            print(voto)
        return sum/len(studente.voti)
            


    def cercastudente(self, nome):
        for i in range(len(self.studenti)):
            if self.studenti[i].nome == nome:
                return self.studenti[i]
            return None
    

class Studente(Persona):
    def __init__(self, nome, eta, voti):
        Persona.__init__(self,nome,eta)
        self.voti = voti

voti = {
    "APA": 9,
    "TAP": 10,
    "ALAN": 2
}
print(type(voti))
studente1 = Studente("Christopher",22,voti)
registro = Registro()
print(registro.addStudente(studente1))
print(registro.media_voti(studente1))
def isRepeated (frase):
    frase = frase.lower()
    frase_spezzata = frase.split(" ")
    parole_ripetute = []
    for word in frase_spezzata:
        if frase.count(word) > 1 and word not in parole_ripetute:
            parole_ripetute.append(word)
    return parole_ripetute
#count è dispendioso
def isRepeated_dict(frase):
    frase_spezzata = frase.lower().split()
    conteggi = {}
    for parola in frase_spezzata:
        conteggi[parola] = conteggi.get(parola,0) + 1
    return conteggi

frase = "Lionel Messi messi è il il giocatore più forte del mondo"
print(isRepeated(frase))
print(isRepeated_dict(frase))

album = {}
album["artista"] = "Anuel"
album["anno"] = 2022

for x,y in album.items():
    print(x,y)


#    for p in parole:
#        if conteggi[p] > 1 and p not in parole_ripetute:
#            parole_ripetute.append(p)