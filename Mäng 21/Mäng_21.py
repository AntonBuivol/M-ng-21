#Mäng 21
import random
kaardipakk=[2,3,4,6,7,8,9,10,11]*4
random.shuffle(kaardipakk)
score=0
start=input("Kas soovid kaarti võtta?? y(yes) n(no): ")
if start=="y":
    while score<21:
        score+=kaardipakk.pop()
        print(f"Sul on {score} punkti")
        if score==21:
            print("Sul on 21 punkti. Sa oled võitnud.")
            break
        if score>21:
            print("Sul on rohkem kui 21 punkti. Sa kaotasid.")
            break
        answer=input("Kas soovid võtta veel kaardi? y(yes) n(no): ")
        if answer=="n":
            break
print(f"Sul on {score} punkti. Head agea!")