name= input("Enter Your Name here:\n ")
mobile= int(input("Enter Your Mobile No. here:\n"))
print("Greetings of the Day, Welcom to Centeral Bank of India, Mr/Mrs",name)
account=(mobile + 2589852345)
balance= 1000
print("Do You want to Check you'r account balance ?")
OP=input("Type Y for Yes and Type N for No \n")
if (OP=='Y'):
    print("You'r Account Balance is,",balance)
elif (OP=='N'):
    print("Thank You, For Connecting with us !!")
else:
    print("You Entered wrong value, Thank You !!")

print("Do You want to Credit or Debit You'r Ammount ?")
CD=input("Type C for Credit and Type D for Debit \n")
if (CD=='C'):
    amount=int(input("Enter Amount here:"))
    sum= balance+amount
    print("You'r Account Balance is,",sum)
elif (CD=='D'):
    amount=int(input("Enter Amount here:"))
    sum= balance-amount
    print("You'r Account Balance is,",sum)
else:
    print("You Entered wrong value, Thank You !!")