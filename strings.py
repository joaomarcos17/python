# strings in python 

my_list = ["Milk","Bread","Porridge","Ice-Cream"]
a = ["Orange", "Apples", "Kiwis"]
my_list.append(a) # you can use my_list.pop() to remove the last element of the list 

print(my_list.index("Bread"))

# this  a  list.sort() function 

def My_function(e): # a length function !!
      return len(e)

cars = ["VW", "Ford", "Fiat"]

cars.sort(key=My_function)

print(cars)
