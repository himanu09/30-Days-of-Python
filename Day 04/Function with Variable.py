# Function with Variable length

def fun1(*num):  
    for n in num:
        print(n)

fun1(10,20,30)
fun1(40,50,60,70)
fun1(80,90,100,110,120)