# Amjad Alakrami
# Alexander Levin
# 05/09/2022

score = 0

Start = print("Hej, Kul att du ville lära dig lite Glossor idag! Vi kör igång")

ord_1 = input("Vad betyder Hund på engelska?").capitalize().replace(" ","")
if ord_1 == "Dog":
    print("Bra Jobbat! Vi går vidare till nästa")
    score += 1  
else:
    print("Attans! Rätt svar är Dog")
ord_2 = input("Vad betyder Katt på engelska?").capitalize().replace(" ","")
if ord_2 == "Cat":
    print("Bra Jobbat! Vi går vidare till nästa")
    score += 1
else:
    print("Attans! Rätt svar är Dog")
ord_3 = input("Vad betyder Bil på engelska?").capitalize().replace(" ","")
if ord_3 == "Car":
    print("Bra Jobbat!")
    score += 1
else:
    print("Attans! Rätt svar är Dog")
print("Då var vi klara för idag. Du fick " + str(score) + " av 3 Rätt")
