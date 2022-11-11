import random
import time

guess = int(input("Adivine el numero entre 0 y 10: "))

numero_rand = random.randint(0, 10)
time.sleep(5)
if guess == numero_rand:
    print("Adivinaste!")
else:
    print("No adivinaste, el numero era", numero_rand)
