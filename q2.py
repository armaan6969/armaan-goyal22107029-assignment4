# question 2


a = int(input("enter the year="))#input year from user
if a<0:
    print("error")
elif (a%100==0 and a%400==0):
    print("It can be a leap year")
elif (a%100==0):
    print("It is not be a leap year")
elif (a%4==0):#divisibility check
    print("It is a leap year")
else :
    print("It is not a leap year")