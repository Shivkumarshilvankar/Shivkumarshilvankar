def num():
    count = 0
    var=int(input("Enter the contact number: "))
    ph=var
    for x in range (20):
        if var != 0:
            count= count + 1
        var = int(var/10)
    if count == 10:
        return ph
    else:
        return "Happy"

def reading(list):
    count = 0
    dict={}
    Lines = list.readlines()
    for line in Lines:
        count += 1
        name=[]
        num=[]
        for x in line.strip():
            if x == "a" or x == "b" or x == "c" or x == "d" or x == "e" or x == "f" or x == "g" or x == "h" or x == "i" or x == "j" or x == "k" or x == "l" or x == "m" or x == "o" or x == "p" or x == "q" or x == "r" or x == "s" or x == "t" or x == "u" or x == "v" or x == "w" or x == "x" or x == "y" or x == "z" or x == "A" or x == "B" or x == "C" or x == "D" or x == "E" or x == "F" or x == "G" or x == "H" or x == "I" or x == "J" or x == "K" or x == "L" or x == "M" or x == "N" or x == "O" or x == "P" or x == "Q" or x == "R" or x == "S" or x == "T" or x == "U" or x == "V" or x == "W" or x == "X" or x == "Y" or x == "Z":
                name.append(x)
            if x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9" or x == "0":
                num.append(x)
        Name=""
        Num=""
        Name=Name.join(name)
        Num=int(Num.join(num))
        dict[Name]=[]
        for x in range (int(len(num)/10)):
            if Num > 0:
                dict[Name].append(int(int(Num)%10000000000))
                Num = int(int(Num)/10000000000)
                #print("1")
    return(dict)

def printing(list,a):
    sourceFile = open('Phonebook.txt', 'a')
    print(str(x) + " : " + str(list[x]), file = sourceFile)
    sourceFile.close()
        


Hale = open('Phonebook.txt', 'r')
Contactlist = reading(Hale)
Hale.close()
print("Do you want to add or View Contactlist")
choice = int(input("Enter 1 for modify and 2 for View: "))
ss = open("PhoneBook.txt", 'r+')
ss.truncate(0)
ss.close()


while choice < 9:
    if choice == 1:
        flag = int(input("Add = 1 upgrade = 2 :"))
        if flag == 1 :
            name=str(input("Enter the Name: "))
            if name in Contactlist:
                print("Already in Contact")
            else:
                i = 1
                while i == 1:
                    contact= num()
                    if type(contact) == int:
                        Contactlist[name]=[]
                        Contactlist[name].append(contact)
                        print("Done")
                        i = 0
                    else:
                        print("Enter a valid number")
        elif flag == 2:
            name=str(input("Enter the Name: "))
            if name in Contactlist:
                i = 1
                while i == 1:
                    contact=num()
                    if type(contact) == int:
                        if contact in Contactlist[name] :
                            print("Already in Conatct")
                        else:
                            Contactlist[name].append(contact)
                            i = 0
                    else:
                        print("Enter a valid number")
            else:
                print("So such Contact")
    elif choice == 2:
        for x in Contactlist:
            printing(Contactlist,x,)   
        ss=open('PhoneBook.txt', 'r')
        print(ss.read())
        ss.close()       
    else: 
        print("Incorrect input")
    
    print("Do you want to view or add Contactlist or leave")
    choice = int(input("Enter 1 for add and 2 for View and 9 for Exit: "))