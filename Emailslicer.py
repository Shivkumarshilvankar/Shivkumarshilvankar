email=str(input("Enter your email Id: "))
clock = 0
a=[]
b=[]
username=""
domain=""
flag = 0

for x in email:
    if "@" in email:
        flag = 1
        if x == "@" and clock == 0:
            clock = 1
        elif x != "@" and clock == 0:
            a.append(x)
        elif x == "." and clock ==1:
            clock=2
        elif x != "." and clock == 1:
            b.append(x)
    else:
        print("Invalid email ID")
        break

username= username.join(a)
domain = domain.join(b)
if flag == 1:
    print("Your username is " + str(username))
    print("And Your domain is " + str(domain))


