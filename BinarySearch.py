a=[96,23,45,74,20,47,23,45,18,27,93,28,63,79,82,34,19,86,65,34,82,74,92,13]
a.sort()
print(a)
num = 74
flag = 0
while flag == 0:
    mid = int(len(a) / 2)
    if a[mid] == num:
        print("Got it")
        flag = 1
    elif a[mid] < num:
        del a[0:mid-1]
        #print("Go more")
    elif a[mid] >  num:
        del a[mid:len(a)]
        #print("Go less")

