# 1st Program
a=input("Enter You'r name here: \n")
b=int(input("Enter You'r age here: \n"))
def details(a,b):
    print("Here is Details of You !,", a ,b)

details(a,b)

# 2nd Program
def fun1(*num):  
    for n in num:
        print(n)

fun1(10,20,30)
fun1(40,50,60,70)
fun1(80,90,100,110,120)

# 3rd Program
def cal(a,b):
    c=a+b
    d=a-b
    print("Sum",c)
    print("Sub",d)
cal(50,60)

#4th Program
def employee_details(name,salary="9000"):
    print("Name:",name,",Salary:",salary)
employee_details("Himanshu",50000)
employee_details("Mohan")

# 5th Program

def outer_fun(a, b):
    square = a ** 2
    def addition(a, b):
        return a + b
    add = addition(a, b)
    return add + 5
result = outer_fun(5, 50)
print(result)

# 6th Program

def num(a):
    if a==0 or a==1:
        return 1
    return a+(a-1)
s=num(10)
print(s)

# 7th Program 

def details(name,age):
    print(name,age)
    
details("Himan",20)
personal =details
personal("Himanshu Rajore,",21)

# 8th Program

print(list(range(4,30,2)))

# 9th Program

x = [4,6,8,24,12,2]
print(max(x))