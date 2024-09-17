#Make a program that greets you at diffrent time

import time

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp1 = time.strftime('%H')
timestamp1 = int(timestamp1)
print(timestamp)


if(timestamp1 < 12):
    print("good morning")
elif(timestamp1 > 12 and timestamp1 < 16):
    print("good evening")
else:
    print("good night")