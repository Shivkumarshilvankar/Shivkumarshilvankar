def prime(num):
    clock = 0
    for x in range (2,num):
        if x < num:
            if num % x == 0:
                clock = 1

    if clock == 0:
            #prime
            return 1

def word(c): 
    s= "" 
    for x in c: 
        s += str(x)    
    return s 

a=[]
b=[]
c=[]
s=""
item_no=[]

item=int(input("Enter the number of item: "))
print("Enter the Item ID: ")
for x in range (item):
    var=int(input())
    item_no.append(var)

for num in item_no:
    if (prime(num)) == 1:
        a.append(num)
    else:
        b.append(num)

c=a+b
print(word(c))