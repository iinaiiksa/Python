import random
import math

# Write a program to print the square root of a number entered from the user @SQRT
x=int(input("Read Numbers"))
print(math.sqrt(x))

# Write a program to print a random name and number 1000 and 10000
# for the number of students input from the user Random

z=int(input("Read Numbers"))
for i in range(1,z,1):
    x = input("Read Name")
    print(x)
    print(random.randint(1000,10000))

#Write a program to print odd numbers between 1 and 10
#Void

def x1():
    for i in range(1,10,1):
        if(i%2==1):
            print(i)
x1()

#Return

def x2():
    msg = ""
    for i in range(1,10+1,1):
        if(i%2==1):
            msg+=str(i)+" "
    return (msg)
print(x2())



# Write a program to print the arithmetic mean of numbers between x and y sent from the main

#VOID

x=int(input("Read Number 1"))
z=int(input("Read Number 2"))
def x1():
    count=0
    sum=0
    for i in range(x,z+1,1):
        count+=1
        sum+=i
    print(sum,sum/count)
x1()
#Return
x=int(input("Read Number 1"))
z=int(input("Read Number 2"))
def x2():
    count=0
    sum=0
    for i in range(x,z+1,1):
        count+=1
        sum+=i
    return(sum,sum/count)
print(x2())

# Print the scores of the successful people, their sums, and the arithmetic mean

def x1():
    grade=int(input("Read Grade -1 For Exit"))
    sum=0
    count=0
    msg=""
    while(grade!=-1):
        if(grade>=60):
            sum+=grade
            count+=1
            msg+=str(grade)+" "
        grade = int(input("Read Grade -1 For Exit"))
    if(count!=0):
        print("Sum",sum," Avg ",sum/count," Msg ",msg)
    else:
        print("No Student")
x1()


def x1():
    grade=int(input("Read Grade -1 For Exit"))
    sum=0
    count=0
    msg=""
    while(grade!=-1):
        if(grade>=60):
            sum+=grade
            count+=1
            msg+=str(grade)+" "
        grade = int(input("Read Grade -1 For Exit"))
    if(count!=0):
        return("Sum",sum," Avg ",sum/count," Msg ",msg)
    else:
        return("No Student")
print(x1())

#Print the odd numbers from 1 to 10

def x1():
    msg=""
    for i in range (1,10,1):
        if(i%2==1):
            msg+=str(i)+" "
    return(msg)
print(x1())

def x1():
    grade=int(input("Read Grade"))
    sum=0
    count=0
    while(grade!=-1):
        if(grade>=60):
            sum+=grade
            count+=1
        grade = int(input("Read Grade -1 For Exit"))
    if(count!=0):
        return (sum,count,sum/count)
    else:
        return ("No Student Pass")
print(x1())

def x1():
    msg=""
    n = int(input("Read Numbers"))
    for i in range(1,n,1):
        if(i%2==1):
            msg+=str(i)+" "
    return(msg)
print(x1())

