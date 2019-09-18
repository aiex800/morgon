#start
#vakna upp
vaken = "n"
#skapar en strängvariabel med värdet n
print("du sover djupt som björnen i ide...") 
while vaken == "n": 
    vaken = input("vaknar du? [y/n]: ").lower() 
#gör en loop
#duscha
print("Du masar dig upp och släpar dig till duschen.")
print("någon har lämnat in brödrost i din dusch")
duscha = input("Flyttar du på brödrosten? [y/n]: ").lower() 
#skriver enfråga
if duscha == "n":
    print("du får frisk vatten över dig")
    print("du känner en stark stöt genom din kropp")
    print("du dör")
    exit() 
#stänger a programet
elif duscha ==("y"):
    print("Friskt vatten sköljer över dig och börjar äntligen vakna")
else:
    print("DOES NOT CONPUTE")

# årstid
season = False
while season == False:
    season = input("vilken årstid är det? [vår, vinter, sommar, höst]: ").lower()
    if season == "vår" or season == "vinter" or season == "höst":
        print("Det är kallt och slask, fyfan")
        print("du klär på dig vinterpälsen...")
        print("Du springer till busstationen")
    elif season == "sommar":
        print("sommar! shorts och flip flops")
    else:
        season = False
season =  "vår" or season == "vinter" or season == "höst"
while season == "vår" or season == "vinter" or season == "höst":
    buss = input("Går du på bussen? y/n: ")
    if buss == "y":
        print("Du går på bussen och sätter dig på sätet längst bak i bussen")
        print("Det sitter en grabb på din plats")
        grabb = input("Frågar du om grabben kan flytta på sig y/n: ")
        if grabb == "y":
            print("Han säger åt dig att det är hans platts nu och att du får sätta dig någon annan stans")
        elif grabb == "n":
            print("Du klämmer knytnävel extra hårt, släger en arg bilck mot grabben och sätter dig bakom han")

            #testlololololololol