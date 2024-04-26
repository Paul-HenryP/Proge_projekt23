#Programmi autorid on Paul-Henry Paltmann ja Elisa Tamm

# Ülesande püstitus: Investorid soovivad teada ettevõtte eelnevate aastate kliendivõrgustiku kasvu. 
# Ettevõte loodi aastal 2010. Ettevõttel on vaja enne koosolekut arvutada kui palju kliente on kuni aastani 2020 iga aasta jooksul keskmiselt nendega liitunud.
# Failis on igal real igal aastal liitunud klientide arv, kusjuures mõnel aastal jäi kliente vähemaks mistõttu on osad arvud negatiivsed.
# 
# 



import math as m
from matplotlib import pyplot as plt
import numpy as np
kliendid = []

intkliendid = [] #uued
negintkliendid = []
posintkliendid = []
#a
avahemik = []
akasv = []
akasvint = []
#b
bvahemik = []
bkasv = []
bkasvint = []
#c
cvahemik = []
ckasv = []
ckasvint = []
keskvaartused = []

negKliendid = []#vana
posKliendid = []#vana

def andmedJärjendiks(fail):
    jarjend = []
    for rida in fail:
        puhasrida = rida.strip()
        jarjend.append(int(puhasrida))
    return jarjend




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
                        print(str(alates + m)+": "+str(kliendid[i])) # m suurendab aastaid igal tsüklil ja print kuvab mitu klienti see aasta liitus
                        avahemik.append(str(alates + m))
                        akasv.append(kliendid[i])
                        akasvint.append(int(kliendid[i]))
                        m += 1 #aasta suureneb iga tsükliga
                        posKliendid.append(int(kliendid[i])) #lisab pos andmed positiivsete andmete globaalsesse järjendisse
                        i += 1 
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
                        bvahemik.append(str(alates + m))
                        bkasv.append(kliendid[i])
                        bkasvint.append(int(kliendid[i]))
                        m += 1
                        negKliendid.append(kliendid[i]) #negatiivsed glob. järjendisse
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
                    cvahemik.append(str(alates + m))
                    ckasv.append(kliendid[i])
                    ckasvint.append(int(kliendid[i]))
                    m += 1
                    i += 1
                    
                else:
                    i += 1
                    
            else:
                i += 1
        
    #f.close()

#küsin kasutajalt täiendavaid andmeid
    
try:
    failNimi = input("Sisestage faili nimi: ")
    #failNimi = "C:\Py code\Projekz\kliendid.txt"
    f = open(failNimi, encoding = "UTF-8")
    for rida in f:
        kliendid.append(rida.strip("\n"))
        intkliendid.append(int(rida.strip("\n")))
    for el in intkliendid:
        if el < 0:
            negintkliendid.append(el)
        elif el >= 0:
            posintkliendid.append(el)
except FileNotFoundError:
    print("Vale faili nimi. Kontrolli, et fail oleks samas kasutas programmi failidega.")

vastus_kolmas = input("Kas soovite Näha aastaid, millal kliente tuli juurde (a), vähenes (b), mõlemat (c) või ei soovi midagi kuvada(x)? ")
#vastus_kolmas = 'a'

if vastus_kolmas == "a":
    alates = int(input("Alates mitmendast aastast soovite informatsiooni arvestada?(2010-2020) "))
    kuni = int(input("Kuni mis aastani soovite informatsiooni arvestada? (2010-2020) "))
    
    if alates < 2010 or alates > 2020: #sisestatud aastate kontroll 
        print("Vigane aasta sisestus.")
    elif kuni < 2010 or kuni > 2020:
        print("Vigane aasta sisestus.")
    else: #käivitab funktsioonid
        loenFailist(vastus_kolmas,alates,kuni) 
        print("Valitud aastate keskmine oli "+ str(round(np.average(posintkliendid),2))+" klienti aastas.")

        #MATPLOTLIB - kuvab alates, kuni ja mis aastatel suurenes klientide arv
        plt.style.use('fivethirtyeight')
        y_vaartused = akasv #vahemik kus pos
        x = 0.5 + np.arange(len(y_vaartused)) #len y peab vastama listi pikkusele

        plt.bar(avahemik, akasvint, color ='maroon', width = 0.4)

        for el in akasvint:
            keskvaartused.append(round(np.average(posintkliendid),2)) #kuvab tulpade arvud

        plt.plot(avahemik, keskvaartused) #aastate keskmiste joon(sinine)
        plt.text(len(avahemik) - 1+0.4, keskvaartused[-1], str(round(keskvaartused[-1], 2)), color='blue', ha='center', va='bottom')

        for i, v in enumerate(akasvint):
            plt.text(i , v, str(v), color='black', ha='center', va='bottom') #for loop kuvab numbreid tulpade kohal

        plt.title("Positiivne klientide muutus")
        plt.ylabel("klientide arv")
        plt.legend(["Keksmine klientide muutus", "Klientide muutus igal aastal"])
        plt.show() #näitab graafikut
    

elif vastus_kolmas == "b":
    alates = int(input("Alates mitmendast aastast soovite informatsiooni arvestada? (2010-2020) "))
    kuni = int(input("Kuni mis aastani soovite informatsiooni arvestada? (2010-2020) "))
    
    if alates < 2010 or alates > 2020: #sisestatud aastate kontroll 
        print("Vigane aasta sisestus.")
    elif kuni < 2010 or kuni > 2020:
        print("Vigane aasta sisestus.")
    else: #käivitab funktsioonid
        loenFailist(vastus_kolmas,alates,kuni)
        print("Valitud aastate keskmine oli "+ str(round(np.average(negintkliendid),2))+" klienti aastas.")
        #MATPLOTLIB - kuvab alates, kuni ja mis aastatel vähenes klientide arv

        plt.style.use('fivethirtyeight')
        y_vaartused = bkasv #vahemik kus neg
        x = 0.5 + np.arange(len(y_vaartused)) #leny peab vastama listi pikkusele

        plt.bar(bvahemik, bkasvint, color ='maroon', width = 0.4)

        for el in bkasvint:
            keskvaartused.append(round(np.average(negintkliendid),2))

        plt.plot(bvahemik, keskvaartused) 
        plt.text(len(bvahemik)-1+0.4, keskvaartused[-1], str(round(keskvaartused[-1], 0)), color='blue', ha='center', va='bottom')
        for i, v in enumerate(bkasvint):
            plt.text(i , v, str(v), color='black', ha='center', va='bottom')

        plt.title("Negatiivne klientide muutus")
        plt.ylabel("klientide arv")
        plt.legend(["Keksmine klientide muutus", "Klientide muutus igal aastal"])
        plt.show()
    
elif vastus_kolmas == "c": #molemad
    alates = int(input("Alates mitmendast aastast soovite informatsiooni arvestada? (2010-2020) "))
    kuni = int(input("Kuni mis aastani soovite informatsiooni arvestada? (2010-2020) "))
    
    if alates < 2010 or alates > 2020: #sisestatud aastate kontroll 
        print("Vigane aasta sisestus.")
    elif kuni < 2010 or kuni > 2020:
        print("Vigane aasta sisestus.")
    else: #käivitab funktsioonid
        loenFailist(vastus_kolmas,alates,kuni)
        print("Aastate keskmine oli "+str(round(np.average(intkliendid),2))+" klienti aastas.")

        #MATPLOTLIB - kuvab alates, kuni ja mis aastatel vähenes ja suurenes
        plt.style.use('fivethirtyeight')
        y_vaartused = ckasv #vahemik kus molemad
        x = 0.5 + np.arange(len(y_vaartused)) #leny peab vastama listi pikkusele
        plt.bar(cvahemik, ckasvint, color ='maroon', width = 0.4)

        for el in ckasvint:
            keskvaartused.append(round(np.average(intkliendid),2))

        plt.plot(cvahemik, keskvaartused)
        plt.text(len(cvahemik)-1+0.4, keskvaartused[-1], str(round(keskvaartused[-1], 0)), color='blue', ha='center', va='bottom')

        for i, v in enumerate(ckasvint):
            plt.text(i , v, str(v), color='black', ha='center', va='bottom')

        plt.title("Klientide muutus")
        plt.ylabel("klientide arv")
        plt.legend(["Keksmine klientide muutus", "Klientide muutus igal aastal"])
        plt.show()


elif vastus_kolmas == "x": #kui ei soovita midagi kuvada
    print("Te ei soovinud midagi kuvada.")
else:
    print("Vigane vastus.")

f.close()
