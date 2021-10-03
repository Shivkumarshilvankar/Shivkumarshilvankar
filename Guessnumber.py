print("Guess a 3 digit number not starting with 0")
print("If less then the shown number then enter 1")
print("If greater then the shown number then enter 2")
print("If equal to the shown number then enter 3")

# Declaration
y=500
clock =1 
a=[500]
z=0

# Algrithm
for x in range (10):
    print ("IS you number" + str(y))
    guess = int(input(""))
    if guess == 1:
        if len(a) <= 1:
            y = int(y/2)
            a.append(y)
            #print("a")
        else:
            if (a[-2]-a[-1])/2 < 0:
                z = (a[-2]-a[-1])/2 * -1
            else:
                z = (a[-2]-a[-1])/2
            y = int(a[-1]-(z))
            if y < 0:
                y = y * -1
            a.append(y)
            #print("b")
    elif guess == 2:
        if len(a) <= 1:
            y = int(y+(y/2))
            a.append(y)
            #print("c")
        else:
            if (a[-2]-a[-1])/2 < 0:
                z = (a[-2]-a[-1])/2 * -1
            else:
                z = (a[-2]-a[-1])/2
            y = int(a[-1]+(z))
            if y < 0:
                y = y * -1
            a.append(y)
            #print("d")
    #print(a)
    elif guess == 3:
        print("Your number is " + str(y))
        break

#print(a)