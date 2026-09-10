import json
import sys

types = []
i = 0
stop = "STOP"

print("Write the types one by one, end with " + stop)

entry = ""

while (entry != stop) :
    print("Write the type n°" + str(i+1))
    entry = input(" :")
    i += 1
    if entry != stop :
        types += [entry]

print("The types are :")
for t in types:
    print(t)

print("\n For each type write the dmg relation to it as an attack move. Ex : Fire is 0.5 towards Water")

type_relationship = {}

for t in types:
    print(t + ":")
    current_elem = {"rel":{}}
    color = input("type color code : ")
    entry =""
    for r in types:
       entry = input("\t" + r + ": ")
       current_elem["rel"][r] = entry
       current_elem["color"] = color
    type_relationship[t] = current_elem
    

print(type_relationship)
with open('relationship_grid.json', 'w') as f:
    json.dump(type_relationship, f, ensure_ascii=False, indent=4)

