import random
i=0
pas = []
UC=""
word = ""
while i < 10:
    ran = random.randint(1,26)
    if ran > 9:
        if i % 3 == 0:
            UC = chr(ran+87).upper()
        else:
            UC = chr(ran+96)
        pas.append(UC)
    elif ran < 10:
        pas.append(str(ran))
    i = i + 1
word = word.join(pas)
print(word)