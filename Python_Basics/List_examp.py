alphabets=["a","b","c","d"]
print(alphabets)
#access
print(alphabets[1])
#back end access
print(alphabets[-1])
#list+strng
msg="alphabet is"
print(msg+alphabets[2])
#modify
alphabets[3]="e"
print(alphabets)
#delete a ele
del alphabets[2]
print(alphabets)
#sort and reverse
alphabets[0]='z'
print(alphabets)
alphabets.sort(reverse=True)
print(alphabets)
alphabets.sort()
print(alphabets)
#length
print(len(alphabets))
#for loop
for alphabets in alphabets:
    print("list=",alphabets)
#range func
for i in range(1,10):
    print(i)
#sum,max,min etc
listNum=[1,2,3,4,5,6,]
print("sum is",sum(listNum))
print("min in list is",min(listNum))
print("max in list is ",max(listNum))
#slicing a list
print(listNum[2:5])
#for loop in list slice
for listNum in listNum[2:4]:
    print(listNum)
#copying list
copyList=listNum[:]
print("new copied list",copyList)