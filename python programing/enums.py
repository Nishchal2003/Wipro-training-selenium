fruits = ["Orange", "cherry" , "kiwi"]
for index,fruits in enumerate(fruits):
    print(index, fruits)

#changing index

fruits = ("Orange", "cherry" , "kiwi")
for index,fruits in enumerate(fruits, start=1):
    print(index, fruits)

word = "python"
for i, ch in enumerate(word):
    print(i, ch)

test_cases = ["Login", "Signup", "Checkout"]
for case_no, test in enumerate(test_cases, start = 1):
    print(f"Executing testcases{case_no}: {test}")

#asccessing of the enumerate values

characters = ["Krillin", "Goku", "Goku", "Picolo",
              "Krillin", "Goku", "Vegeta", "Gohan", "Picolo"]

character_map = {character: [] for character in set(characters)}

for index, character in enumerate(characters):
    character_map[character].append(index)

print(character_map)
