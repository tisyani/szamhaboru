import random

random_number = random.randint(1,6)

answer = int(input("Kérlek adj meg egy számot: "))

if answer > random_number :
    print("Nyertél!")
elif answer < random_number :
    print("Vesztettél!")
elif answer == random_number : 
    print("Döntetlen")

print (f"{random_number} volt a szám.")