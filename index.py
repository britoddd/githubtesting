'''
name = input("Name: ")
print(f"Hello, {name}")

n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")
'''


'''
index = "Budi"
print(index[0])
# B
'''

# Define a list of name
names = ["Budi", "Siti", "Joko", "Joko", "Joko", "Siti"]
print(names[2]) # Joko

names.append("Draco")
print(names)

names.sort() # Ngurutin sesuai abjad
print(names)

coordinate = (10.0,20.0)


s = set()
print(s)

s.add(1)
s.add(2)
s.add(2) # Ga bisa ngeadd yang udah ada di situ
print(s)

s.remove(2) # Splice
print(s)

print(F"The set has {len(s)} elements")

# tapi kalo ada angka yang dobel, bakal cuma nongol satu 

for i in [0, 1, 2, 3, 4, 5]:
    print(i)

aName = "Potter"
for letter in aName:
    print(letter)

listName = ["Potter", "Granger", "Weasley"]
for name in listName:
    print(name)

#

houses = {"Harry": "Griffindor", "Draco": "Slytherin"}

houses["Hermione"] = "Griffindor"

print(houses)
print(houses["Harry"])

#

from function import square  # python file name, function name

for i in range(10):
    print(f"The square of {i} is {square(i)}")

# another method
'''
from function 
for i in range(10):
    print(f"The square of {i} is {function.square(i)}")  # harus dikasih penjelasan nama filenya
'''