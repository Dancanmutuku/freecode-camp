price=20
print(price)

"""
full_name="Steve Biko"
age=20
is_new=True
"""

#user input
fav_colour=input("what is your fav colour")
print("Hey your Favourite colour is"+fav_colour)
gender=input("What is your gender?")
print("Hi Dan your gender is "+ gender)

birth_year =input("birth year")
age=2019-int(birth_year)
print(age)

#quiz
weight_lbs=input("weight (lbs)")
weight_kgs=float(weight_lbs)*0.45
print(weight_kgs)

#string
course='''
hi dan welcome 
how can i help you today
thank you
'''
print(course)
print(course[3])

#string methods
name2="Python geek"
print=(name2.capitalize)
print(2536%3)
print(10**3)
x=10
x = x+3
print(x)

is_hot =False
is_cold=True
if is_hot:
    print("its a hot day")
    print("Drink a cold beer")

elif is_cold:
    print("its a cold day ")
    print("Drink a warm beer")
else:
     print("Its a lovely day")
     
print("Enjoy your day")