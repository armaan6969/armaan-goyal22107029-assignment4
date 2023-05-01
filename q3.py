# question 3
#module random
import random as r

for i in range(11):
    a= r.randint(1,10)
    b= r.randint(1,10)
    answer = a*b
    print("Question", i+1,a,"x",b)
    
    answeruser= int(input(""))
    
    
    if answeruser==answer:
        print("answer is correct")
    else:
        print("wrong\n","answer is",a*b)