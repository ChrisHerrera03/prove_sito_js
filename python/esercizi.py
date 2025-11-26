def pari_dispari(n):
    return n % 2 == 0

#num = int(input("Numero: "))
num = 0
try:
    if pari_dispari(num):
        print("Pari")
    else:
        print("Dispari")
except:
    print("Problema grosso")


def max(list):
    max = -1
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

list = [7,20,4]
print(max(list))

def conta_vocali(parola):
    cont_vocali = 0
    for i in range(len(parola)):
        match parola[i]:
            case 'a'|'e'|'i'|'o'|'u':
                cont_vocali = cont_vocali+1
    return cont_vocali    
    
print(conta_vocali("aeiou"))

def inverti(parola):
    parola_inver = []
    i = len(parola) - 1
    while i >= 0:
        parola_inver.append(parola[i])
        i-=1
    return "".join(parola_inver)
print(inverti("ciao"))

list = [1,3,1,2,5,5]
def duplicati(lista):
    newlist = []
    for i in range(len(lista)):
        k = i+1
        for k in range(len(lista)):
            if(i != k and lista[i] == lista[k]):
                newlist.append(lista[i])
    return newlist

print(duplicati(list))

