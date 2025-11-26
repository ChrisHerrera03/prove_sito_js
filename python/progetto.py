class Car:
    def __init__(self, modello, anno):
        self.modello = modello
        self.anno = anno

    def descrizione(self):
        print(f"Macchina: {self.modello} dell'anno {self.anno}")

macchine = [Car("Fiat",1999),Car("Opel",2002),Car("Lamborghini",2024)]

for i in range(len(macchine)):
    if macchine[i].anno > 2000:
        macchine[i].descrizione()

thisdict = {
    "Crazy": 1,
    "colors": ["red","yellow"]
}
thislist = ["apple","banana"]
thislist.insert(0,"lollo")
print(thislist)
print(thisdict["colors"][0])
macchine.pop(2)
del macchine[1]
name = input("devi")