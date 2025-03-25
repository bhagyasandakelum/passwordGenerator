import random

upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lover_letters = upper_letters.lower()

digits = "0123456789"

syms= "!@#$%^&*()_+"

upper, lower, nums, symbols = True, True, True, True

all = ""

if upper:
    all += upper_letters
if lower:
    all += lover_letters
if nums:
    all += digits
if symbols:
    all += syms

length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)