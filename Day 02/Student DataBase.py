Library = { 1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
            7: {},
            8: {},
            9: {},
            10:{}}

for i in range (1,11):
    print("Student No.", i )
    ST = input("Enter Student Name: \n")
    P = int(input ("Enter Physics Mark: "))
    C = int(input ("Enter Camistry Mark: "))
    M = int(input ("Enter Maths Mark: "))

    Library[i]["Name"]=ST
    Library[i]["Physics"]=P
    Library[i]["Camistry"]=C
    Library[i]["Maths"]=M

for j in range(1,11):
    print(Library[j])