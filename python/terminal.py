#import time

#sec = int(input("Inserisci secondi: "))

#for x in range(sec, 0, -1):
#    print(x)
#    print(f"{x:02} secs") #02 fa 0numero
#    time.sleep(1)


numeri = set([1,1,1,-1,3])
numeri = [num for num in numeri if num>0]
print(numeri)

grades = [85,44,32]
passing_grades = [grade for grade in grades if grade > 60]
print(passing_grades)