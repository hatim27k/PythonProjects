items = ["apple", "chiku", "orange", "grape"]
for item in items:
    print(f"Buying {item}")

items.append("kiwi")
print("Updated shopping list:", items)

find = "kiwi2"

def matcher(items, find):
    for item in items:
        if item == find:
            return True
    return False

if matcher(items, find):
    print(f"Found a {find} in the list! {items}")

for i, item in enumerate(items):
    print(f"Item {i + 1}: {item}")
    if item == find:
        print(f"Found a {find}, yay!")
        break
else:
    print(f"No {find} found in the list.")

vector = (5, 2, 3)
print("Vector:", vector)
print("Vector length:", len(vector))

x, y, z = vector
print(f"x: {x}, y: {y}, z: {z}")

person = {"name": "John", "age": 30, "city": "New York"}

import sys

print("Person details:" + str(person) + " " + str(type(list(person.keys()))))