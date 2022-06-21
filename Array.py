
x=[2,5,6,9,]
for i in x:
    print(i)

#odd numbers

x=[2,4,7,11,]
count=0
for i in x:
    if(i%2==1):
        print(i)
        count+=1
if(count==0):
    print("No Odd Numbers")

# array sum
sum=0
x=[2,5,6,9,]
for i in x:
    sum+=i
print(sum)




# add the odd numbers

x=[5,6,7,8,9,]
sum=0
for i in x:
    if(i%2==1):
        sum+=i
print(sum)

# Add variables from the user

x=[]
for i in range(3):
    x.append(input("Read Number"))
print(x)

#or

x=[]
for i in range(3):
    num=int(input("Read Number"))
    x.append(num)
print(x)

# Add the variable to a specific location
x=[1,2,3,4,5]
x.insert(2,50)
print(x)

#Delete a specific item
x=[1,2,3,4,5]
x.remove(3)
print(x)

#Delete a locator element
x=[1,2,3,4,5]
x.pop(3)
print(x)

# delete the entire array

x=[1,2,3,4,5]
x.clear()
print(x)

# Locate the element in the array
x=[1,2,3,4,5]
z=x.index(3)
print(z)

# Finding the iterations of a given element
x=[1,2,3,4,5,3]
z=x.count(3)
print(z)

# inverse matrix
x=[1,2,3,4,5,3]
print(x)
x.reverse()
print(x)

# Arrange the array from smallest
x=[7,3,5,7,9]
print(x)
x.sort()
print(x)

# Arrange the array from largest to smallest
x=[7,3,5,7,9]
print(x)
x.sort()
x.reverse()
print(x)

# Copy an array to another array
x=[7,3,5,7,9]
y=x.copy()
print(y)

# Add the number of elements from one array to another or from the user
x=[7,3,5,7,9]
y=[44,55]
x.extend(y)
print(x)


#or
x=[7,3,5,7,9]
x.extend([44,55])
print(x)


# enter scores
#highest successful score
#highest score
x=[]
y=[]
for i in range(5):
    num=int(input("Read Number"))
    if(num>=60):
        x.append(num)
    else:
        y.append(num)
print("max Pass",max(x))
print("max Fail",max(y))


#Print the passing grades, the sum, the arithmetic mean, and the largest degree, and arrange them in descending order
# In the event that there is no blatant student, a message appears
#add 90 70 85


x=[]
y=[]
for i in range(3):
    grade=int(input("Read Number"))
    if(grade>=60):
        x.append(grade)
    else:
        y.append(grade)
print("Print Array ",x,y)
if(len(x)>0):
    if (len(x) > 0):
        print("Pass ",x)
        print("Sum ", sum(x))
        print("Avg ", sum(x) / len(x))
        print("Max ", max(x))
        x.sort(reverse=True)
        print(x)
    else:
        print("Error")
x.extend([85,70,90])
print(x)



x=[]
for i in range(5):
    grade=int(input("Read Grade"))
    x.append(grade)
print(x)


#2
x_pass=[]
for i in range(3):
    if(x[i]>=60):
        x_pass.append(x[i])
if(len(x_pass)>0):
    print(x_pass)
    print("Sum ",sum(x_pass))
    print("Avg ",sum(x_pass)/len(x_pass))
    print("Max ",max(x_pass))
    x_pass.sort(reverse=True)
    print(x_pass)
else:
    print("Error")

#3
x.extend([85,70,90])
print(x)

#Delete the scores of repeaters
for k in range(6):
    for i in x:
        if(i<60):
            x.remove(i)
print(x)





