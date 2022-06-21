'''
Write a program to print the arithmetic mean of the odd numbers
 Between two numbers entered by the user and then print the numbers
'''


sum=0
count=0
i=0
while(i>=0):
    i = int(input("Enter Any Number .. -1 to exit  "))
    if(i>=0):
        if(i%2==1):
            sum+=i
            count+=1
        i+=1

if(count!=0):
    print("Sum: ",sum,"Avg: ",sum/count)
else:
    print("i<x")

# Write a program to print the total scores of students entered by the user

i=1
sum1=0
count1=0
msg=""
v = int(input("How Many Student :"))

while(i<=v):
    mark = int(input("Read Mark :"))
    if(mark>=60):
        msg+=str(mark)+" "
        sum1+=mark
        count1+=1
    i+=1

if(sum1 !=0):
    print("grades ",msg)
    print("Sum ",sum1)
    print("Count ",count1)
    print("Avg ",sum1/count1)

else:
    print("No Student")


#Print the grades as well as the arithmetic average of the grades of successful
# people entered from the user for the number of N students
msg=""
i=1
count=0
sum=0
v = int(input("How Many Student :"))
if(v>0):
    while(i<=v):
        mark = int(input("Read Mark :"))

        if(mark>=60):
            sum += mark
            msg += str(mark) + " "
            count += 1
        i+=1
    if(count!=0):
        print("Count",count)
        print("SUM =: ",sum)
        print(" AVG =:",sum / count)
        print(" Mark Students ",msg)

    else:
        print("All Students Are Fail")
else:
    print("No Student")



#1 - get out of loop

sum=0
count=0
grade=int(input("Read Grade "))

while(grade!=-1):
    if (grade >= 60):
        count += 1
        sum+=grade
    grade=int(input("Read Grade or -1 for exit: "))

if(sum==0):
    print("No Student")
else:
    if (count != 0):
        print("Sum: ", sum, "Avg: ", sum / count, " Count ", count)
    else:
        print("All Student is Fail ....")




        
