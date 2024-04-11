'''
1)
Using print() will print anything
between the parentheses into your console.

Change the phrase being printed below, 
save, and then view your changes 
in the console.

After confirming that it works, comment it out.
'''
print("space project") #23pm
#print("hello me")

'''
2)
Using both the (+) and the (*) operators,
multiply and add any combination of numbers
together so that you get the number 10.
'''
a = 2
b = 4
c = 2
result = a * b + c
print(result)
# print() alterei esse pra testar a logica 
#e deu super certo
'''
3)
print() is often used to debug
issues. You can actually add multiple
arguments inside of print() (which are
separated by a comma). Add everything
below into print()!
'''
print(3 + 4, "should equal 7")
# print(3 + 4, " should equal 7")

'''
#TODO
4)
Add two strings together so that you
are printing your full name!
'''
a = "el toro "
b = "indultado "
result = a + b 
print (result) 
# print() troquei tambem pra mostrar que eu
#fiz o exercicio 


'''
5)
Change Mia's location by reassigning the location
variable to a new string! To do this, you will have 
to add a new line of code (do not delete any currently
written code). Note: you will also have to un-comment
the print to print the location.
'''
#TODO
name = "Mia"
current_location = "school"
print(name, " is currently at ", current_location)
# essa tambem entendi
'''
6)
Create variables so that the message is printed
to the screen!
'''
person = "Jordi "
place = "born "
food = "pizza "
print(person, " went to the ", place, " to eat ", food, ".")
# esse eu me quebrei por erro bobo de sintaxe
#tenho duvidas sobre isso "."
#TODO
# print(person, " went to the ", place, " to eat ", food, ".")

'''
7)
Now, reassign all the previous variables so that
a new message is printed to the screen!
'''
person = "jaume "
place = "gotico "
drink = "beer "
print(person, " went to the ", place, " to drink ", drink, ".")

#TODO
# print(person, " went to the ", place, " to eat ", food, ".")

'''
8)
There are three ways to increase the
number stored in the variable "count".
However, there is a problem with how 
the variable has been declared. Debug it!
'''

count = 0
count = count + 1
count += 1
count += 1

print(count, " should be 3")


'''
9)
Swap time! In the code below, we want to swap
the values being stored in both "a" and "b".

This code written below does not work. To accomplish
this task, you will need to create an additional
variable (you can name it "temp") to store either
"a" or "b" while you are swapping. Draw it out if
you are unsure!
'''

a = 1
b = 2

print("BEFORE > a is: ", a, " - and b is: ", b)

temp = a
a = b
b = temp

print("AFTER > a is: ", a, " - and b is: ", b)

'''
10)
Make the statement below evaluate
to true!
'''
#TODO

print(3 < 4)
#print (not(3 > 4))
'''
11)
Make the statement below evaluate
to false.
'''
#TODO
x = 10
y = x

print(not(x <= y))

'''
12)
Fix the comparison operator so that
the statement evaluates to false.
'''
print (3 != 3)

#TODO
#print(3 == "3")

'''
13)
Change something in the expression below
so that it does not evaluate to false.
'''

sunny = True
warm = True

print(sunny == warm)

'''
14)
Practice with everything you've learned so far!

Come up with 10 expressions that use what
you've learned so far.
    - Use the data types: string, int, float, boolean, null.
    - Use the following operators: (+) (-) (*) (/).
    - Use the operators: (=) (+=) (-=) (*=)(++) (--).
    - Use the operators: (>) (<) (>=) (<=) (== vs ===) (!=).
'''

''' eu consegui fazer mas tenho duvidas, 1 achei que tinha 
apagado e reiniciado, mas foi salvo, vou te perguntar sobre isso
sobre o not nas booleans tambem vou te perguntar'''

#1
city = "barcelona "
verb = "tiene "
verb1 = "poder "
print (city + verb + verb1) 

#2
a = 50
b = 13
print(a - b)

#3,4
banana = 56.12
abacate = 13.47
print(banana * abacate)
print(banana / abacate)

#5
print(23 > 8)

#6 
estreladalva = 7
estreladalva += 5
print(estreladalva)

#7
mt = "gondor "
ca = "numenor "
print("o povo do oeste veio de ", mt, "e se estabaleceu em ", ca,)
print(not("o povo do oeste veio de ", mt, "e se estabaleceu em ", ca,))
print("o povo do oeste veio de ", ca, "e se estabaleceu em ", mt,)
print("true")
print(" i love tolkien ")

#8
print(8 < 7)
#false

#9 
print(9 > 5)
#true

#10
print(25 == 25)
#true

#11
print (27 != 27 )
#false

''' sorry for the time... *o* '''


