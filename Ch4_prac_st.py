#problem1: write a program to store 7 fruits in a list entered by the user.
fruit =[]

f1 = input("enter fruit name: ")
fruits.append(f1)
f2 = input("enter fruit name: ")
fruits.append(f2)
f3 = input("enter fruit name: ")
fruits.append(f3)
f4 = input("enter fruit name: ")
fruits.append(f4)
f5 = input("enter fruit name: ")
fruits.append(f5)
f6 = input("enter fruit name: ")
fruits.append(f6)
f7 = input("enter fruit name: ")
fruits.append(f7)

print(fruits)

list= ("apple","orange","banana","mango","graphes","watermelon","cherry")

#problem2: write a program to accept marks of 6 students and display them in a sorted manar.

marks = []
f1 = int(input("enter marks here: "))
marks.appens(f1)
f2 = int(input("enter marks here: "))
marks.append(f2)
f3 = int(input("enter marks here: "))
marks.append(f3)
f4 = int(input("enter marks here: "))
marks.append(f4)
f5 = int(input("enter marks here: "))
marks.append(f5)
f6 = int(input("enter marks here: "))
marks.append(f6)

marks.sort()
print(marks)

# problem3 : check tuple type can not be changed.

a = (34,234,"khushi")

a[2]= cherry # ye changed nhi hoga kyuki tuple immutable hota h

# problem4: write a program to use a list with four numbers.

l = (4,5,5,6)

print(sum(l)) #output : 20

#problem 5: write a program to count the no. of zeros in the following tuple

a = (7,0,8,0,0,9)

n= a.count(0)
# output : zero= 3




