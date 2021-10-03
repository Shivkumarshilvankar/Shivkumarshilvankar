class Clock:
    def __init__(self,a,num,counter,p):
        self.a = a
        self.a[num] = p 

def Winner(a,b,c):
    if a == b == c != " ":
        print(" __________________")
        print("| " + str(a + " is the winner |"))
        print(" -------------------")
        return 1
    else:
        if flag == 1:
            return 1
        else:
            return 0


def XO(a):
    if a % 2 == 0:
        return ("X")
    else:
        return ("0")


a=[" "," "," "]
b=[" "," "," "]
c=[" "," "," "]
counter = 0
list = []
out = []
flag = 0

print("Welcome to Tic tac toe.")
print("You have to enter the number")
print("The number 1 to 9 going from left top to right bottom.")
print("First player is X")
print("Second Player is O")
print("Hope You like it.")
print("Let's begin")
print(a)
print(b)
print(c)

while counter < 10:
    if counter > 2:
        flag = Winner(out[0],out[1],out[2])
        flag = Winner(out[3],out[6],out[0])
        flag = Winner(out[4],out[8],out[0])
        flag = Winner(out[7],out[4],out[1])
        flag = Winner(out[4],out[6],out[2])
        flag = Winner(out[5],out[8],out[2])
        flag = Winner(out[4],out[5],out[3]) 
        flag = Winner(out[7],out[8],out[6])
        if counter == 9 and flag == 0:
            print("Draw")
            break
    if flag == 1:
        break
    num = int(input("Enter the place: "))
    var = num
    p = XO(counter)
    if (var in list):
        print ("NO overwrite. Try again")
        counter = counter
    else:
        list.append(var)
        if num < 10 and num != 0:
            if num <= 3:
                Clock(a,num-1,counter,p)
            elif num <= 6:
                Clock(b,(num%3)-1,counter,p)
            elif num <= 9:
                Clock(c,(num%3)-1,counter,p)
            print(a)
            print(b)
            print(c)
            out = a + b + c
            counter = counter + 1
        else:
            print("Invalid input")
            conuter = counter