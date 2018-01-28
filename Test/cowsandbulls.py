import random

x= random.randint(1000,9999)

x = str(x)

count=0
c=0
y=0
while x != y:
        c=0
        b=0
        y = input(" GUESS THE 4-DIGIT NUMBER : ")
        for i in range(0,len(x)):
            if x[i] == y[i]:
                c=c+1
            if c==4:
                break
        else:
            print(" COWS = ", c  ," and BULLS = ", 4-c)
        count=count+1

print("WELL YOU HAVE GUESSED THE NUMBER IN ", count ,"ATTEMPTS")
