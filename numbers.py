def mynum():
    return 3+9

x=mynum()

#comment

print(x)


#strings

"hello"

mystring="hello world"
print(mystring[2])

#slicing perfrom by [:]

print(mystring[:2])

print(mystring[::2])

#format method

x="Insert another string here:{}".format("INSERT ME!")
print(x)

mylist=['p',1,4]

mylist[1]="x"
mylist.append(45)
print(mylist)

y=mylist.pop(0)
print(y)
print(mylist)

mylist.reverse()

print(mylist)
print(mylist)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_colomn=[row[0] for row in matrix]

print(first_colomn)

mydic={"name":123,"key":"value1"}
print(mydic['key'])


#Loops

seq = [1,2,3,4,5,6]

for jelly in seq:
    print(jelly)

for k in mydic:
    print(k)
    print(mydic[k])


#tupel unpacking

mypairs=[(1,2),(3,4),(5,6)]

for(tup1,tup2) in mypairs:
    print(tup2)
    print(tup1)