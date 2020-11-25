str=input("Introduceti sirul de caractere: ")
m=0
c=0
cs=0
for simbol in str:
    m+=simbol.isupper()
print("in sir sunt",m,"majuscule")
for simbol in str:
    c+=simbol.isdecimal()
print("sirul are",c,"cifre")
for simbol in str:
    if simbol.isalnum():
        continue
    if simbol.isspace():
        continue
    else:
        cs+=1
print("sirul are",cs,"caractere speciale")
