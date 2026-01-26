#!/usr/bin/python3


num = int(input("enter a number : "))


if num < 10:
    print(num)

else:
    last = num % 10
    print(last) 

 ch = input('enter a single character:')
if ch.lower() in "aeiou":
    print("it is a vowel")
else:
    print("it is not a vowel") 

""" num = int(input("enter a number"))
if num % 2 == 0:
    print("given number is even")
else:
    print("given number is odd") """

 # WAP to calculate percentage of a student through 5 subjects. Take marks as input from the user.
# Using percentage print which grade the student has scored.

""" m = int(input("enter the number for math:" ))
p = int(input("enter the number for phy:" ))
c = int(input("enter the number for chem:"))
bio = int(input("enter the number for bio:"))
e = int(input("enter number for eng:"))
sub_marks = m + p + c + bio + e
total_mark=int(input("enter maximum marks"))
perc = (sub_marks/total_mark)*100

if perc>90:
    print("you have got A+ grade")
elif perc<=90 and perc>80:
    print("you have got Agrade") """

rows = 5 # Number of rows

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ") # Print star and a space without a newline
    print() # Move to the next line after the row is printed

side = 5

for i in range(side):
    for j in range(side):
        print("*" ,end="")
    print()
