import random
import string

panjang = int(input("Input your password length : "))

if panjang <= 0:
    print("Input must be greater than 0")
else:
    simbol = "!@#$%^&*"
    karakter = string.ascii_letters + string.digits + simbol

    password = ""

    for _ in range(panjang):
        password += random.choice(karakter)

    print("Password :", password)