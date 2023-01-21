#MD5
import hashlib
password = "texto"
md5 = hashlib.md5(password.encode())
print("The corresponding MD5 hash is : ")
print(md5.hexdigest());
