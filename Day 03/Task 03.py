a= input("Enter You'r name: \n")
b= input("Enter Gender here (M/F): ")
c= {'Mango':'90 Rs/KG',
'Apple':'120 Rs/KG',
'Banana':'60 Rs/KG',
'Coconut':'40 Rs/Pis'}
if (b=="M"):
    print("Greeting of the day, Mr", a)
elif(b=="F"):
    print("Greeting of the day, Mis", a)
else:
    print("You entered wrong Gender !!")
print("Today's Offer: Shop more than 100Rs & get 80% OFF")
print("Choose any one item from given blow list:")
print(c)
d=input("Enter you'r choise here from above options: ")
e=int(input("Enter Quantity of item in KG: "))
if (d=="Mango"):
    f=e*90
    print("You'r Total Amount is: Rs",f)
elif (d=="Apple"):
    f=e*120
    print("You'r Total Amount is: Rs",f)
elif (d=="Banana"):
    f=e*60
    print("You'r Total Amount is: Rs",f)
elif (d=="Coconut"):
    f=e*40
    print("You'r Total Amount is: Rs",f)

if (f>=100):
    print("Congratulation, You have won a Discount Coupon upto 80% OFF !! \n Here is the coupon code: (himanu10)")
    g=input("Did You want to use Coupan Yes/No \n")
    i=input("Enter Coupon Code here:")
    if(g=="Yes"):
        if (i=="himanu10"):
            j=(f-((f*80)/100))
            print("Congratulation you have to pay only: Rs",j)
        else:
            print("You Entered Wrong Code !")
    else:
        print("You have to Pay: Rs",f)

print("Thank You for Shopping with Us :) ")