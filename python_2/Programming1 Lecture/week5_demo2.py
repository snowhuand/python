words = {}
words["avalanche"] = """
1. a large mass of snow, ice, etc., detached from a mountain slope and sliding or falling suddenly downward.
2.anything like an avalanche in suddenness and overwhelming quantity:
an avalanche of misfortunes; an avalanche of fan mail.
3.Also called Townsend avalanche. Physics, Chemistry. a cumulative ionization process in which the ions and electrons of one generation undergo collisions that produce a greater number of ions and electrons in succeeding generations.
"""

#plants = {} # key is name, value is the color
plants = {"carrot":"orange",
          "raddish": "white",
          "beetroot": "red"
          }
plants["mango"] = "yellow"

#for each in plants: #return the key
 #   print("Getting plant:{}, value: {}".format(each, plants[each]))
#print(plants)

#print(plants.items())
for key, value in plants.items():
    print("{:10s} -> {:10s}".format(key, value))

#for value in plants.values():
 #   print(value)

names = ["John", "John", "Ann", "Jane"] #list of names
count = {}

for each in names:
    if each in count:
        count[each] += 1
    else:
        count[each] = 1
#print(count)