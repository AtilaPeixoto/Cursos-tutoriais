import random
from time import sleep

n = random.randint(1,10)
nu = int(input("tente adivinhar o numero "))


if n == nu:
  ok = "Pensei em {} tambem...\n PARABENS!!!".format(n)
else:
    ok = "Haaa. Pensei em {}.\nTente de novo. Voce  vai conseguir!".format(n)
    
    
sleep(3)

print("--=--" * 20)
print(ok)