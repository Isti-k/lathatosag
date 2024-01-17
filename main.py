import masik
#változók hatóköre és láthatósága
"""globális változók azok a változók amik adott fáljban is elérhető"""
"""lokális változó adott eljáráson/függvényben elérhető"""
"""eljárásoknak és függvényeknek paramétert két módon adhatunk át értékszerint és címszerint
értékszerinti paraméter átadás: egyszerű adatszerkezet esetén pl:int,str,boolin stb.
cimszerinti paraméterátadás: összetett adatszerkezet esetén pl:lista,tömb"""
"""értékszerinti paraméter átadás estén egy másolat készül a változóban és ezért lokális változóként működik az eljárásban az az eljáráson belül az értéke megváltoztatható, azonban ez semmien hatásra nincs az eljáráson kívüli értékre
cimszerinti paraméteres átadaás ha a válzotó változó értékét az eljáráson belül megváltoztathatjuk akkor az eljáron kívül is változik fog általa megadott paramétere."""


szoveg:str="Első szöveg" #globalis változó ebben a modulban látszik

print(szoveg)

#print(szoveg2) #ez a változó itt nem látszik.

def eljaras():
    szoveg:str="Másik szöveg eljárásban"
    print(szoveg)
    szoveg2:str="eljárásban"
    print(szoveg2) #lokális változó csak az eljárásban érhető el.

eljaras()

print(szoveg)
#print(szoveg2)

def masikeljaras():
    #print(masikvalami) name 'masikvalami' is not defined
    print(valami) #cannot access local variable 'valami' where it is not associated with a value
    valami:str="valami"

#masikeljaras()

# érték szerinti paraméterátadás

################### egyszerű adattípus, int, string
def elj2(valt:int):
    valt+=1
    print(valt) #13


valt=12

elj2(valt)

print("valt",valt) #valt,12

# cím szerinti paraméterátadás

################### összetett adattípus, lista
def elj3(lista):
    lista[0]=11111111111
    for i in range(0,len(lista),1):
        print(lista[i])

lista=[1,2,3,4,5,6,7]

elj3(lista)

for i in range(0,len(lista),1):
    print("lista az eljárás hívása után",lista[i])







