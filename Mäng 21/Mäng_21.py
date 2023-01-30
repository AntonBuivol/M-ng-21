#Mänd 21
import random
kaardipakk=[2,3,4,6,7,8,9,10,11]*4
random.shuffle(kaardipakk)
score=0
start=input("Kas soovid kaarti võtta?? y(yes) n(no): ")
n=1
if start=="y":
    while n<4:
        score+=kaardipakk.pop()
        print(f"Sul on {score} punkti")
        answer=input("Kas soovid võtta veel kaardi? y(yes) n(no): ")
        if score==21:
            print("Sul on 21 punkti. Sa oled võitnud.")
            break
        if score>21:
            print("Sul on rohkem kui 21 punkti. Sa kaotasid.")
            break
        if answer=="y":
            n+1
else:
    print(f"Sul on {score} punkti. Head agea!")