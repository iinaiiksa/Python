


# Prints numbers from 1 to 9
for i in range(1,10,1):
    print (i)

# Print the odd numbers between 1 and N
n=int(input("Read N"))
if(n>1):
    for i in range(1,n,1):
        if(i %2 == 1):
            print (i)
else:
    print("N<1")
    

# Print the even numbers between two numbers entered by the user

x=int(input("Read x"))
z=int(input("Read z"))

if(x<z):
    for i in range(x,z,1):
        if(i %2 == 0):
            print (i)
else:
    print("X>=Z")


#Print PASS and FAIL for 5 students

for i in range(0,5,1):
    mark = int(input("Read Mark :"))
    if(mark>=60):
        print ("Pass")
    else:
        print("Fail")

# Print the sum of 6 numbers entered by the user
sum=0
for i in range(0,6,1):
    number = int(input("Read number :"))
    sum+=number
print("Sum Numbers is= : ",sum)


#Print the arithmetic mean of the scores of the successful students only for the number N

sum=0
count=0
n=int(input("How Many Students: "))
for i in range(0,n,1):
    mark = int(input("Read Mark :"))
    if(mark>=60):
        sum += mark
        count+=1
if(count>0):
    print("The number of successful students =: ",count)
    print("The total number of successful students =: ",sum)
    print("The average number of successful =: ",sum/count)
else:
    print("No Student Pass")



'''
Print the arithmetic average of the scores of successful students
Only for an unlimited number of students
-1 exit condition
'''

sum=0
count=0
grade=int(input("Read grade: "))
for i in iter(int, 1):
    if(grade==-1):
        break
    if(grade>=60):
        sum += grade
        count+=1
    grade=int(input("Read Grade or -1 for exit: "))

if(count>0):
    print("The number of successful students =: ",count)
    print("The total number of successful students =: ",sum)
    print("The average number of successful =: ",sum/count)
else:
    print("No Student Pass")
