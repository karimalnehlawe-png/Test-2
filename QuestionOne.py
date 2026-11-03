import time
from random import choice

day = time.strftime("%A")
month = time.strftime("%B")
date = int(time.strftime("%d"))

print(f"The lucky numbers for {day}, {month} {date} are --->", end=" ")

for i in range(8):
    print(choice(range(2, 901)), end=" ")

print()
