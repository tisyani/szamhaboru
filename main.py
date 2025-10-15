import random

random_number = random.randint(1,6)

answer = int(input("Kérlek adj meg egy számot 1-6-ig: "))

if answer > random_number and answer < 7:
    print("Nyertél!")
elif answer < random_number :
    print("Vesztettél!")
elif answer == random_number : 
    print("Döntetlen")
elif answer not in [1, 2, 3, 4, 5, 6]:
    print("Csak 1-től 6-ig lehet számot megadni")

print (f"{random_number} volt a szám.")