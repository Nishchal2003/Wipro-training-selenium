country = {"India" : "Delhi",
           "Canada" : "Ottawa",
           "England" : "London"}
print(country)
print(country["India"])
my_dict = {1 : "One",
           2: "Two",
           3 : "Three"}
print(my_dict)
my_dict = {1 : "One", 2: "Two", 3 : "Three",1 : "Four"}
print(my_dict)


#Tuples as a key
my_dict = {(1,2) : "One" "Two",3 : "Three"}
print(my_dict)
#List of key
#$my_dict = {1 : "Hello", [1,2] : "Three"}
#print(my_dict)

country.pop("Canada")
print(country)

my_dict.update({4 : "Four"})
print(my_dict)

print(my_dict.keys())