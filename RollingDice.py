import random
i=0

print("This is rolling dice game should we start.")
print("Type y for Yes and n For No")
choice = str(input("y/n: "))
while i < 1:
    if choice == "y" or choice == "Y" or choice == "yes" or choice =="YES" :
        var = int(random.randint(1,6))
        num = int(random.randint(1,6))
        if var == num:
            print("Woow! double " + str(num))
        else:
            print("You got " + str(num) + " and " + str(var))
    if choice == "n" or choice == "N" or choice == "no" or choice =="NO":
        i = 3
    if i == 0:
        choice = str(input("Want to try again? : "))

print("Thank You for giving me a chance.")
print("Come back again.")

