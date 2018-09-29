print("welcome to the bank application")
print("enter name")
name=input()
print("enter the age")
age=input()
print("enter the address")
address=input()
print("enter the salary")
salary=input()
print("enter the empid")
empid=int(input())
print("checking number of years in company")
print("-----------------------")
if empid >=1000:
    print("2years of expirence")
else:
    print("more than 2 years of expirence")
list=[name,age,address,salary,empid]
for list in list:
    print(list)