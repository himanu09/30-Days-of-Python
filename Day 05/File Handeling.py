import json


file = open('json.txt','w+')
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
dict = {'name': name, 'age': age, 'city': city}
json.dump(dict,file)
file.sk(0)
print(file.read()) 
print(type(file.sk))