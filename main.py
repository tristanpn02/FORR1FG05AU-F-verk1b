##########################
# Tristan Pétur Andersen #
# 23 Ágúst 2018          #
# Æfingaverkefni 1b      #
##########################

#Býr til breytur
karl = 'Jon'
kona = 'Sno'
kronur = 150
skonumer = 35

#Gerir "block" sem að keyrir eftirfarna línur
def lidurA():
    #Sækir breytur
    global karl
    global kona
    global skonumer
    global kronur
    
    #Skrifar línu
    print(karl + " keypti skónúmer " + str(skonumer) + " fyrir " + kona + " sem kostuðu " + str(kronur) + " krónur")
    
    #Bætir 2 við breytuna "skonumer"
    skonumer = skonumer+2;
    
    #Skrifar línu
    print('En þá mundi hann að hún notar skónumer ' + str(skonumer))
    
    
def lidurB():
    #Tekur innslátt og setur þær í breytur
    tala1 = int(input('Sláðu inn tölu 1: '))
    tala2 = int(input('Sláðu inn tölu 2: '))
    tala3 = int(input('Sláðu inn tölu 3: '))
    
    #Setur saman tölurnar og setur summu í breytu
    summa = tala1 + tala2 + tala3
    #Margfeldir saman tölurnar og setur margfeldi í breytu
    margfeldi = tala1 * tala2 * tala3
    #Frádráttur talna og setur í breytu
    fradrattur = tala1 - tala2 - tala3
    
    #Skrifar línu
    print('Summa talnanna er: ' + str(summa) + "\nMargfeldi talnanna er: " + str(margfeldi) + "\nFrádráttur talnanna er: " + str(fradrattur))
    
#Keyrir lið A
lidurA()
input("\nLiður A lokið, ýttu á enter til þess að fá lið B\n")

#Keyrir lið B
lidurB()