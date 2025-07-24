#!/bin/python3

print("Importing is Important")

import sys
from datetime import datetime
print(datetime.now())
from datetime import datetime as dt
print(dt.now())
def new_line():
   print('\n')
new_line()
print("Advanced Strings: " )
my_name= "Jerry"
print(my_name[0])
print(my_name[-1])
sent ="STARMAN  WAITING IN THE SKY"
print(sent[:4])
print(sent[-3:])
print(sent.split())

print("Dictionry are keys and values");
drinks={"white Russians": 7, "Old Fashion": 10, "Lemon Drop": 8, "Buttery Nipple":  6 }
print(drinks)

employees ={"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr", "Mort"]}
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)
drinks['White Russians']  = 8
print(drinks)


movie = "The Batman"
print("My fav movie is {}.".format(movie))

print(drinks.get("white russians"))
print(drinks.get("Matin"))
# print(drinks['White Russains'])

movies =["Superman", "Batmman", "Spiderman"]
person=["clark", "Bruce", "Peter"]
combined =zip(movies, person)
movie_dic = {key: value for key, value in combined}

print(movie_dic)
 


