#odd numbers
i=int(input("Read i :"))
x=int(input("Read x :"))

print("Odd Number :")
while(i<x):
    if(i%2==1):
        print(i)
    i+=1
   
print("Even Number :")
while(i<=x):
    if(i%2==0):
        print(i)
    i+=1
# If i is greater than x it gives the wrong message
if (i > x):
    print("X < i")
else:
    while (i < x):
        if (i%2==0):
            print(i)
        i += 1


# Students with a grade above 60 passed
i=1
v = int(input("How Many Student :"))
if(v>0):
    while(i<=v):
        mark = int(input("Read Mark :"))
        if(mark>=60):
            print("Pass")
        else:
            print("Fail")
        i+=1
else:
    print("No Student")

# collect numbers with loop
i=1
s=0
while(i<=5):
    s+=i
    i+=1
print(s)