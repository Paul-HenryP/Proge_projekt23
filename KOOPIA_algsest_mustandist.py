#Programmi autor on Paul-Henry Paltmann
#Viimane muudatus: 21.03.2022

# Ülesande püstitus: Investorid soovivad teada ettevõtte eelnevate aastate kliendivõrgustiku kasvu. 
# Ettevõte loodi aastal 2010. Ettevõttel on vaja enne koosolekut arvutada kui palju kliente on eelneva 10 aasta jooksul keskmiselt nendega liitunud.
# Failis on igal real igal aastal liitunud klientide summa, kusjuures mõnel aastal jäi kliente vähemaks mistõttu on osad arvud negatiivsed.
# 
# 
# Programm küsib kasutajalt: 
#                            Faili nime, mis on samas kaustas thonny failidega. (kliendid.txt)
#                             
#                            Mis aastast alates ning mis aastani soovitakse andmeid lugeda.
#                            Kas, kui üldse, soovitakse väljastada ka aastaid, kus kliente jäi vähemaks, tuli juurde või mõlemat.  
# 
# Lahendus:                 Funktsioon, mille argumentideks on faili nimi ja arvestatavate aastate algus ja lõpp aastad, tagastab mitu klienti
#                           on keskmiselt aastate vahemikus liitunud.
#                           Faili andmed loetakse funktsioonis järjendisse, et andmeid sealt edasi kasutada.
#                           Programm, mis kuvab, mis aastatel on kas liitunud või vähenenud kliente või mõlemad.



#panen kirja algsed andmed, järjendid ja funktsioonid
import math as m
kliendid = []
negKliendid = []
posKliendid = []

def keskmine(vastus): #keskmise arvutaja #selle saaks tegelt asendada math moodulist average funktsiooniga
    summa = 0
    jagaja = 0
    
    if vastus == "a":
        for el in posKliendid: #loeb järjendist, kus on ainult pos. arvud
            
            summa += int(el) #klientide kogusumma jagatud klientide arvuga, kordub b ja c puhul.
            jagaja += 1
        kesk = summa/jagaja
        return kesk
    elif vastus == "b":
        for el in negKliendid: # loeb neg klientide järjendist
            
            summa += int(el)
            jagaja += 1
        kek = summa/jagaja
        return kek
    else:
        for el in kliendid: #loeb järjendist, kus on nii pos kui neg arvud
            
            summa += int(el)
            jagaja += 1
        keskm = summa/jagaja
        return keskm



def loenFailist(midaLoen,algusaasta,lõppaasta):
    algusaasta = algusaasta - 2010 #arvutab andmete asukoha järjendis 
    lõppaasta = lõppaasta - 2010
    i = 0
    if midaLoen == "a": #positiivsete klientide arvudega aastad
        m = 0
        while i < len(kliendid): #analüüsitakse iga aasta klientide arv eraldi läbi
            
            if i >= algusaasta:
                
                if i <= lõppaasta:
                    if int(kliendid[i]) > 0:  #positiivsed arvud
                        print(str(alates + m)+": "+str(kliendid[i])) # m on õigete aastate kuvamise jaoks
                        m += 1 #aasta suureneb iga tsükliga
                        posKliendid.append(kliendid[i]) #lisab pos andmed positiivsete andmete järjendisse
                        i += 1 # tsükli lugeja suureneb
                    else:
                        m += 1 
                        i += 1
                else:
                    i += 1
                    
            else:
                i += 1 #põhimõte kordub b ja c puhul väikeste erinevustega
    elif midaLoen == "b": #neg klientide aastad
        m = 0
        while i < len(kliendid): #analüüsitakse iga element eraldi läbi
            
            if i >= algusaasta:
                
                if i <= lõppaasta:
                    if int(kliendid[i]) < 0:   # negatiivsed
                        print(str(alates + m)+": "+str(kliendid[i]))
                        m += 1
                        negKliendid.append(kliendid[i]) #negatiivsed järjendisse
                        i += 1
                    else:
                        m += 1
                        i += 1
                else:
                    i += 1
                    
            else:
                i += 1
        
        
    else:
        m = 0
        while i < len(kliendid): #analüüsitakse iga element eraldi läbi
            
            if i >= algusaasta:
                
                if i <= lõppaasta:
                    print(str(alates + m)+": "+str(kliendid[i])) # nii positiivsed kui negatiivsed aastad
                    m += 1
                    i += 1
                    
                else:
                    i += 1
                    
            else:
                i += 1
        
    f.close()

#küsin kasutajalt täiendavaid andmeid
    
try:
    failNimi = input("Sisestage faili nimi: ")
#del#failNimi = "kliendid.txt"

    f = open(failNimi, encoding = "UTF-8")
except FileNotFoundError:
    print("Vale faili nimi.")
for rida in f:
    kliendid.append(rida.strip("\n"))

vastus_kolmas = input("Kas soovite Näha aastaid, millal kliente tuli juurde (a), vähenes (b), mõlemat (c) või ei soovi midagi kuvada(x)? ")


if vastus_kolmas == "a":
    alates = int(input("Alates mitmendast aastast soovite informatsiooni arvestada?(2010-2020) "))
    
    kuni = int(input("Kuni mis aastani soovite informatsiooni arvestada? "))
    
    if alates < 2010 or alates > 2020: #sisestatud aastate kontroll 
        print("Vigane aasta sisestus.")
    elif kuni < 2010 or kuni > 2020:
        print("Vigane aasta sisestus.")
    else: #käivitab funktsioonid
        loenFailist(vastus_kolmas,alates,kuni) 
        print("Valitud aastate keskmine oli "+ str(round(keskmine(vastus_kolmas),2))+" klienti aastas.")
    

elif vastus_kolmas == "b":
    alates = int(input("Alates mitmendast aastast soovite informatsiooni arvestada? "))
    kuni = int(input("Kuni mis aastani soovite informatsiooni arvestada? "))
    
    if alates < 2010 or alates > 2020: #sisestatud aastate kontroll 
        print("Vigane aasta sisestus.")
    elif kuni < 2010 or kuni > 2020:
        print("Vigane aasta sisestus.")
    else: #käivitab funktsioonid
        loenFailist(vastus_kolmas,alates,kuni)
        print("Valitud aastate keskmine oli "+ str(round(keskmine(vastus_kolmas),2))+" klienti aastas.")
    
elif vastus_kolmas == "c":
    alates = int(input("Alates mitmendast aastast soovite informatsiooni arvestada? "))
    
    kuni = int(input("Kuni mis aastani soovite informatsiooni arvestada? "))
    
    if alates < 2010 or alates > 2020: #sisestatud aastate kontroll 
        print("Vigane aasta sisestus.")
    elif kuni < 2010 or kuni > 2020:
        print("Vigane aasta sisestus.")
    else: #käivitab funktsioonid
        loenFailist(vastus_kolmas,alates,kuni)
        print("Aastate keskmine oli "+str(round(keskmine(vastus_kolmas),2))+" klienti aastas.")
elif vastus_kolmas == "x": #kui ei soovita midagi kuvada
    print("Te ei soovinud midagi kuvada.")
else: # vigase vastuse kontroll
    print("Vigane vastus.")
    

f.close()
