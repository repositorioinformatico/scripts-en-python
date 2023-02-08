#MD5
import hashlib
import random
for x in range(1,100000):
 i = random.randrange(1,1000) #Ruben's idea
 password = str(i)
 md5 = hashlib.md5(password.encode())
 print("El hash para el numero " + str(i) + " es " + md5.hexdigest())
