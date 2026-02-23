stud_id = {112,113,114,115,116,117,50}
print(stud_id)

letters = {'a','b', 'c', 'd', 'e' }
#print((letters))

letters.add(50)
#print(letters)
copy = letters.copy()
#print(copy)

diff = letters.difference(stud_id,copy)
#print(diff)

#letters.difference_update(stud_id)
#print(letters)

jnt = letters.isdisjoint(stud_id)
#print(jnt)

letters.discard('a')
#print(letters)

inter = letters.intersection(stud_id)
print(inter)

#inter_update = letters.intersection_update(stud_id)
#print(inter_update)

print(letters.union(stud_id))
print(max(stud_id))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


