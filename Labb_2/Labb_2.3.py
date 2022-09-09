# Amjad Alakrami
# Alexander Levin
# 09/09/2022

Eng = ["Car", "Dog", "Cat"] #skapa en lista 
Sve = ["Bil", "Hund", "Katt"] #skapa en lista 
score = 0 #skapa variabel
chans = 3 #skapa variabel

for i in range(0, len(Eng)): #loopar igenom listan Eng
    question = input("Vet du vad " + Eng[i] + " betyder på Svenska ?").capitalize()  #skapar en input variabel 
    if question == Sve[i]: #om användarens svar är rätt
        print("Bra! Det var rätt") #skriv ut
        score +=1 # lägg till en etta i score
    else: #annars
        print("Dåligt! Rätt svar är ", Sve[i]) #skriv ut det istället

# den här loopen kommer köras tills användaren svarar rätt eller inte har några chanser kvar. 
while True: # skapar en while loop 
    if chans > 0: # om chans inte är större än noll 
        hard_question = input("Vet du vad utrikesdepartementet betyder på Eng? Du har " + str(chans) + " försöka på dig :)") #skapar en input variabel
        if hard_question == "Ministry of Foreign Affairs": # om användaren svarar rätt 
            print("JÄTTE BRA JOBBAT!!") #skriv ut  
            score +=1 #lägg till en etta  till score 
            break #avsluta while-loopen
        else: #annars
            chans -= 1 #ta bort en etta från chans 
            print("Ajdå, det var tyvär fel") #skriv ut 
    else: # om chans inte är större än 0 
        break #avsluta while-loopen

print("Då var vi klara för idag! Du fick ", score, "av 4 rätt")