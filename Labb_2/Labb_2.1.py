# Amjad Alakrami
# Alexander Levin
# 09/09/2022
namn1=input("Vad heter kastare 1: ") #definerar en input variabel 
namn2=input("Vad heter kastare 2: ") #definerar en input variabel 
poang1=[] #definerar en lista
poang2=[] #definerar en lista
spelar1_tot = 0 #definerar en int variabel
spelar2_tot = 0 #definerar en int variabel
for i in range(5): #skapar en for-loop för att för att ställa frågan x-antal gånger (x = 5 i det här fallet)
    poang=int(input("Vilken poäng fick "+namn1+ " på kast nr "+str(i+1)+ ": ")) #definerar en input variabel 
    poang1.append(poang) #lägger till poang i lisatan poang1
for i in range(5): #skapar en for-loop för att för att ställa frågan x-antal gånger (x = 5 i det här fallet)
    poang2.append(int(input("Vilken poäng fick "+namn2+" på kast nr "+str(i+1) + ": "))) #lägger till användares  matning i lisatan poang2
for i in poang1: #loopar igenom listan poang1
    spelar1_tot += i #adderar ihop alla värden i listan poang1 och lagrar det i variabel spelar1_tot
for i in poang2: #loopar igenom listan poang2
    spelar2_tot += i #adderar ihop alla värden i listan poang2 och lagrar det i variabel spelar2_tot

if spelar1_tot > spelar2_tot: # if-sats för att kolla om spelar1_tot > spelar2_tot
    print(namn1, "vann med ", str(spelar1_tot-spelar2_tot), "poäng skillnad") #då skriver vi ut det här 
elif spelar1_tot < spelar2_tot: #elif-sats för att kolla om spelar1_tot <  spelar2_tot
    print(namn2, "vann med ", str(spelar2_tot-spelar1_tot), "poäng skillnad") #då skriver ut det här
else: #om varken if-statsen eller elif-satsen är sanna
    print("Det blev lika!") #skri ut det här
