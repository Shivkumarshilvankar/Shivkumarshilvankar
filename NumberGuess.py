import random
num = random.randint(100,999)
i = 0 
print(num)
print("This is a guessing games.")
print("We have a 3-digit number in our mind. Let's call it Var.")
print("You will have 10 chance ot guess the number.")
flag = 0

while i < 10:
    print("You have " + str(10-i) + " chance to guess the 3-digit number.")
    guess = int(input("Your guess will be: "))
    if guess < 100:
        print("The number you entered is less then 3-digit. Try again!")
    elif guess > 999:
        print("The number you entered is more than 3-digit. Try again!")
    elif guess < num :
        print("GO higher.Try again!")
        i = i + 1
    elif guess > num:
        print("Go lower. Try again!")
        i = i + 1
    elif guess == num:
        flag = 1
        break
    
if flag == 0:
    print("Better luck next time")
elif flag == 1:
    print("Yah! You have entered the right number.")