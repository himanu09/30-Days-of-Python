class Calculator:
    def Addition (self,a,b):
        return a+b
    def Subtraction (self,a,b):
        return a-b
    def Multiplication (self,a,b):
        return a*b
    def Division (self,a,b):
        return a/b
    def SquareRoot (self,a):
        return a**(1/2)
    def CircumferenceOfCircle (self,a):
        return 2*(22/7)*a

class Calsi:
    def CompoundInterest (self,p,r,t):
        return (p*(1+(r/100))**t)-p

val1=Calculator()
val2=Calsi()
print("Welcome To The Calculator")
Choice = 1
while Choice!=0:
    print("Choose from the option given below")
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Compound Interest")
    print("7. Circumference Of Circle")
    c=int(input("Enter You'r Choice here: "))

    if c==0:
        print("Exited")
    elif c==1:
        a=int(input("Enter 1st No. here:"))
        b=int(input("Enter 2st No. here:"))
        print("Result",val1.Addition(a,b))
    elif c==2:
        a=int(input("Enter 1st No. here:"))
        b=int(input("Enter 2st No. here:"))
        print("Result",val1.Subtraction(a,b))
    elif c==3:
        a=int(input("Enter 1st No. here:"))
        b=int(input("Enter 2st No. here:"))
        print("Result",val1.Multiplication(a,b))
    elif c==4:
        a=int(input("Enter 1st No. here:"))
        b=int(input("Enter 2st No. here:"))
        print("Result",val1.Division(a,b))
    elif c==5:
        a=int(input("Enter No. here:"))
        print("Result",val1.SquareRoot(a))
    elif c==6:
        p=int(input("Enter Initial Principal here:"))
        r=int(input("Enter Rate of Interest here:"))
        t=int(input("Enter no. Time Periods(in Year):"))
        print("Result",val2.CompoundInterest(p,r,t))
    elif c==7:
        a=int(input("Enter Radius here:"))
        print("Result:",val1.CircumferenceOfCircle(a))
    else:
        print("Invalid value!!")