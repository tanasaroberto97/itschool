def CNP () :
    while True:
        try:
            CNP = int(input("CNP angajat : "))
        except ValueError:
            CNP = "eroare"
            print("CNP trebuie sa fie de tip integer ! ")
        if len(str(CNP)) == 13 :
            break
        else:
            print("CNP trebuie sa fie egal cu 13 cifre ! ")
    return CNP

def Nume() :
    while True : 
        verificare = 0
        Nume = input("Nume angajat : ")
        for item in Nume :
            if item.isdigit() :
                verificare = verificare + 1
        if verificare == 0 and len(Nume) != 0  :
            break
        elif verificare != 0 :
            print('Numele trebuie sa fie numai cu litere') 
        elif len(Nume) == 0 :
            print("Numele trebuie sa fie scris !")
    return Nume
    
def Prenume() :
    while True : 
        verificare = 0
        Prenume = input("Prenume angajat : ")
        for item in Prenume :
            if item.isdigit() :
                verificare = verificare + 1
        if verificare == 0 and len(Prenume) != 0  :
            break
        elif verificare != 0 :
            print('Prenumele trebuie sa fie numai cu litere') 
        elif len(Prenume) == 0 :
            print("Prenumele trebuie sa fie scris !")

    return Prenume

def Departament() :
    while True : 
        verificare = 0
        Departament = input("Departament angajat : ")
        for item in Departament :
            if item.isdigit() :
                verificare = verificare + 1
        if verificare == 0 and len(Departament) != 0  :
            break
        elif verificare != 0 :
            print('Departamentul trebuie sa fie numai cu litere') 
        elif len(Departament) == 0 :
            print("Departamentul trebuie sa fie scris !")

    return Departament

def Varsta() :
    while True :
        verificare = 0
        Varsta = input("Varsta angajatului : ")
        for item in Varsta :
            if item.isalpha() :
                verificare = verificare + 1
        if verificare == 0 and len(Varsta) !=0 :
            break
        elif verificare != 0:
            print("Varsta trebuie sa fie numai numeric !")
        elif len(Varsta) == 0 :
            print("Varsta trebuie introdusa !")
    return Varsta

def Salar() :
    while True :
        verificare = 0
        Salar = input("Salariul angajat : ")
        for item in Salar :
            if item.isalpha() :
                verificare = verificare + 1
        if verificare == 0 and len(Salar) !=0 :
            break
        elif verificare != 0:
            print("Salariul trebuie sa fie numai numeric !")
        elif len(Salar) == 0 :
            print("Salariul trebuie introdus !")
    return Salar

def Senioritate() :
    conditie=["junior" , "mid" , "senior"]
    while True :
        Senioritate = input("Senioritatea angajatului : ")
        if len(Senioritate) == 0 :
            print("Senioriatea trebuie introdusa !")
        elif Senioritate not in conditie :
            print("Senioritatea trebuie sa fie junior mid sau senior")
        elif Senioritate in conditie : 
            break
    return Senioritate

# CNP Nume Prenume Departament Varsta Salar Senioritate

#    1) Adaugare angajat
#   2) Cautare angajat (dupa CNP)
#   3) Modificare date angajat (dupa CNP)
#   4) Stergere angajat
#   5) Afisare angajati
#   6) Calculator cost total salarii
#   7) Calculator cost total salarii departament
#   8) Calculator fluturas salar angajat (CAS - 10% din brut, CASS - 25% din brut, Impozit - 10% din ce a ramas)
#   9) Afisarea angajatilor (dupa senioritate)
#   10) Afisarea angajatilor (dupa departament)
#   11) Iesire

def afisare_meniu():
    print("\n")
    print("1)Adaugare angajat")
    print("2)Cautare angajat dupa CNP")
    print("3)Modificare date angajat dupa CNP")
    print("4)Stergere angajat")
    print("5)Afisare angajati")
    print("6)Calculator cost total salarii")
    print("7)Calculator cost total salarii departament")
    print("8)alculator fluturas salar angajat CAS")
    print("9)Afisarea angajatilor dupa senioritate")
    print("10)Afisarea angajatilor dupa departament")
    print("11)Iesire")
    print("\n")

def adaugare() :
    cnp = CNP()
    nume = Nume()
    prenume = Prenume()
    departament = Departament()
    varsta = Varsta()
    salar = Salar()
    senioritate = Senioritate()
    angajat = [cnp,nume,prenume,departament,varsta,salar,senioritate] 
    return angajat


def optiune() :
    lista_optiuni = ["1","2","3","4","5","6","7","8","9","10","11"]
    while True : 
        intrare = input("Selectati optiunea de mai sus : ")
        if intrare not in lista_optiuni:
            print("Selectati o optiune de mai sus !")
        if intrare in lista_optiuni :
            break
    return intrare

def cautare_angajat_cnp (list) :
    cnp = CNP()
    raspuns=[]
    if len(list) == 0 :
        print("Nu avem angajati !")
    else :
        for item in list:
            if cnp in item:
                raspuns.append(item)
            else:
                print("Nu exista angajat ! ")
    print(raspuns)

def modificare_date_angajati(list) :
    list=adaugare()
    return list

def modificare_dupa_cnp (list) :
    cnp = CNP()
    if len(list) == 0 :
        print("Nu avem angajati !")
    else:
        for item in list :
            if cnp in item :
                list=modificare_date_angajati(item)
    print(list)

def stergere_angajati(list):
    cnp=CNP()
    if len(list) == 0 :
        print("Nu avem angajati !")
    else:
        for item in list:
            if cnp in item:
                list.remove(item)
    return list
        
def afisare_angajati(list):
    for item in list :
        print(item)

def cost_total_salarii(list):
    rezultat=0
    if len(list) == 0:
        print("Nu avem angajati !")
    else:
        for item in list:
            rezultat=rezultat+int(item[5])
    print("Cost total salarii :")
    print(rezultat)

def cost_total_departament(list):
    rezultat=0
    departament=Departament()
    if len(list) == 0 :
        print("Nu avem angajati ! ")
    else:
        for item in list :
            if departament == item[3]:
                rezultat=rezultat+int(item[5])
    print("Cost dupa departament :")
    print(rezultat)

def salariul(list):
    rezultat=0
    cnp=CNP()
    if len(list) == 0 :
        print("Nu avem angajati !")
    else:
        for item in list:
            if item[0]==cnp:
                rezultat=rezultat+ int(item[5]) - int(item[5])/10 - int(item[5])/4 - int(item[5])/10
    print("Salar dupa CAS !")
    print(rezultat)

def afisare_senioritate(list):
    senioritate=Senioritate()
    lista_afisare=[]
    if len(list) == 0 :
        print("Nu avem angajati !")
    else:
        for item in list:
            if item[6]==senioritate:
                lista_afisare.append(item)
    print("Lista dupa senioritate :")            
    print(lista_afisare)

def afisare_departament(list):
    departament=Departament()
    lista_afisare=[]
    if len(list)==0 :
        print("Nu avem angajati !")
    else:
        for item in list:
            if item[3]==departament:
                lista_afisare.append(item)
    print("Lista dupa departament :")
    print(lista_afisare)


def program () : 
    angajati=[]
    while True : 
        afisare_meniu()
        print("\n")
        print(angajati)
        print("\n")
        intrare=optiune()
        print("\n")
        if intrare == "1" :
            print("Adaugare angajat ! \n")
            angajati.append(adaugare()) 
        elif intrare == "2" :
            print("Cautare angajat dupa CNP ! \n")
            cautare_angajat_cnp(angajati)
        elif intrare == "3" :
            print("Modificare angajat dupa CNP ! \n")
            modificare_dupa_cnp(angajati)
        elif intrare == "4" :
            print("Stergere angajat !")
            stergere_angajati(angajati)
        elif intrare == "5" :
            print("Afisare angajati !")
            afisare_angajati(angajati)
        elif intrare=="6":
            cost_total_salarii(angajati)
        elif intrare=="7":
            print("Cost departament !")
            cost_total_departament(angajati)
        elif intrare=="8":
            print("Salariu dupa CAS !")
            salariul(angajati)
        elif intrare=="9":
            print("Afisare dupa senioriate :")
            afisare_senioritate(angajati)
        elif intrare=="10":
            print("Afisare dupa departament  :")
            afisare_departament(angajati)
        elif intrare == "11" : 
            break
            print("Ati iesit din program !")
    

program()



