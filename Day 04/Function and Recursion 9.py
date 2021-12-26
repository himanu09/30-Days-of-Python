# Create a function in Python
a=input("Enter You'r name here: \n")
b=int(input("Enter You'r age here: \n"))
def details(a,b):
    print("Here is Details of You !,", a ,b)

details(a,b)

# Create a function with variable length of arguments
def fun1(*num):  
    for n in num:
        print(n)

fun1(10,20,30)
fun1(40,50,60,70)
fun1(80,90,100,110,120)

# Return multiple values from a function
def cal(a,b):
    c=a+b
    d=a-b
    print("Sum",c)
    print("Sub",d)
cal(50,60)

# Create a function with default argument
def employee_details(name,salary="9000"):
    print("Name:",name,",Salary:",salary)
employee_details("Himanshu",50000)
employee_details("Mohan")

# Create an inner function to calculate the addition in the following way

def outer_fun(a, b):
    square = a ** 2
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5
result = outer_fun(5, 50)
print(result)

# Create a recursive function

def num(a):
    if a==0 or a==1:
        return 1
    return a+(a-1)
s=num(10)
print(s)

# Assign a different name to function and call it through the new name
def details(name,age):
    print(name,age)
    
details("Himan",20)
personal =details
personal("Himanshu Rajore,",21)

# Generate a Python list of all the even numbers between 4 to 30

print(list(range(4,30,2)))

# Find the largest item from a given list

x = [4,6,8,24,12,2]
print(max(x))