# Amjad Alakrami
# Alexander Levin
# 09/09/2022

konsonanter="bcdfghjklmnpqrstvwxz"  #skapar en variabel med alla konsonanter 
rövarspråk="" #definerar en töm string 
print("Hej välkommen till rövarspråksöversättaren") #skirv ut  
svenska=input("Vilken bokstav vill du översätta:").lower() # skapar en input o lagrar den i variabel svenka 
for i in svenska: #loppar igenon det som användaren mattade in i svenksa-input
    bokstav = i #lagra i (alltså varje tecken från svenksa) i bokstav
    if i in konsonanter: #kollar om något tecken är en konsonant genom att kolla om tecknet finns i "konsonanter"
        bokstav += "o"+i #om så är fallet så lägger vi till ett o och sedan samma bokstav igen
    rövarspråk += bokstav   # lagar boksat i rövarspråk 
 

print("Översättningen blir: " + rövarspråk) #skriv ut