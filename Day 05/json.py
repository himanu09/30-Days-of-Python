import json

file = open('json.txt','w+')
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
dict = {'Name': name, 'Age': age, 'City': city}
json.dump(dict,file)
file.seek(0)
print(file.read()) 
print(type(file.seek))