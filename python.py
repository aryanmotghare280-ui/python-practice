
#accept the radius  and print area and cicumference of the circle
radius = int(input("enter the radius here :"))
area =  3.14 * radius*radius
circumference = 2 * 3.14 *radius
print("the area of the cicle is :",area , "the cicumference of the circle is ",circumference)

#accepts the marks of the three subjects and print total and percentage
sub1=int(input("enter the subject 1 marks :"))
sub2=int(input("enter the subject 2 marks :"))
sub3=int(input("enter the subject 3 marks :"))
total = sub1 + sub2+ sub3
percentage = (total/300)*100
print("the total marks is :",total,"the percentage of all subjects is:",percentage )

#accepts 3 numbers and print greater number
n1 =int(input("enter the number 1 here :"))
n2 =int(input("enter the number 2 here :"))
n3 =int(input("enter the number 3 here :"))
if n1>n2 and n1>n3:
    print("n1 is greater number")
elif n2>n3 and n2>n3:
    print("n2 is greater number ")
else:
    print("n3 is greater number ")
    
#accepts the 2 numbers and operator and print result
a= float(input("enter the first number here :"))
b= float(input("enter the second number here :"))
op =input("enter the operator (+,-,*,/): ")
if op =="+":
    print("the addition of the two numbers is :",a+b)
elif op =="-":
    print("the subtraction of the two numbers is :",a-b)
elif op =="*":
    print("the multiplication of the two numbers is :",a*b)
elif op =="/":
    print("the division of the two numbers is :",a/b)

#accepts the character and print the vowel is present or not
char = input("Enter the character here: ")

if any(vowel in char.lower() for vowel in "aeiou"):
    print("Vowel is present in the character")
else:
    print("No vowel is present in the character")

#discount on the shopping bill
bill = float(input("enter the bill amount here :"))
if bill <1000:
    print("no discount")
elif bill >1000 and bill <=5000:
    print("5 % discount on the bill",bill*0.5)
elif bill > 5000:
    print("10 % discont is appicable ", bill *0.10)

#accept temperature  print "hot" , normal or cold
temp=float(input("enter the temperature "))
if temp > 40 :
    temperature = "hot"
elif temp >=20 and temp <40 :
    temperature = "normal"
elif temp <20:
    temperature ="cold"
print("the temperature is ",temperature)

#check the greater number among in three numbers
n1 = int(input("enter the first number "))
n2 = int(input("enter the second number "))
n3 = int(input("enter the third number "))
if n1 >n2 and n1 >n3:
    print(n1,"the n1 is greater")
elif n2>n1 and n2>n3 :
    print(n2,"n2 is greater")
else :
    print(n3,"n3 is greater ")


#accept n1,n2 and operator from user
#check if operator is "+" then add n1 and n2
#else check if operator is"-" then sub...
#else check if operator is"*" then multiply

n1 = int(input("enter the number 1 :"))
n2 = int (input("enter the number 2 :"))
op = input("enter the operator (+,-,*,/)")
if op == "+":
  print("the addition is",n1+n2)
elif op =="-":
  print("subtraction is",n1-n2)
elif op =="*":
  print("multiplication is ",n1*n2)

#vowel or not
ch = input("entere the character here:").lower
if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    print("Vowel")
else:
    print("not Vowel")


temp = float(input("enter the temperature :"))
if temp <=10 :
    print("cold")
elif temp <=20:
    print("normal")
elif temp <=30:
    print("pleasant")
else:
    print("hot")

billamount =float(input("enter the bill amount here :"))
discount =0
if billamount<=1000:
    discount=0
elif billamount <=5000:
    discount=billamount * 0.5
else :
    discount=billamount*0.10
print("discount is :",discount)
total = billamount -discount
print("total pyable amount is ",total)

#number divisible 3 and 5 , only by 5 and only by 3
num = int(input("enter the number :"))
if num % 3 ==0 and num % 5 == 0:
    print("divisible by 3 and 5")
elif num % 3 == 0 :
    print("divisible by 3")
elif num % 5 ==0 :
    print("divisible by 5")
else :
    print("not divisible by 3 or 5 ")

years = float(input("enter the number of years :"))
if years <=1:
    print("interest is 5 % ")
elif years <=3:
    print("interest is 7 % ")
else:
    print("interest is 10 % ")


ch = input("enter the character ")
if ch.isupper():
    print("Upper Case")
elif ch.islower():
    print("Lower Case")
elif ch.isdigit():
    print("digit")
else:
    print("speacial character ")

#program to accept  username and password and check whether username= admin and password = admin123
username=input("enter username")
password = input("enter password")
if username=="admin" :
    if password =="admin123":  #nested if if ke andr ek aur if
        print("login successful")
    else:
        print("invalid password")
        
else:
    print("invalid username")

#Product Discount Cateogory (Pricing Analysis)
#situation: You are analyzing inventory and need to decicde the discount category for a product based on its current stock
#Rules :Stock <=10 = "clearance sale(40% off)"
#stock 11-30 = "heavy discount(25% off")
#stock 31 - 100 = "regular discount(10 % off)
#stock > 100 = "no discount"

stock =int(input("enter the stock "))
if stock <=10:
    print("clearance sale : 40% off")
elif stock <=30:
    print("heavy discount 25%")
elif stock <=100:
    print("regular discount 10 %")
else:
    print("No discount")

tenure = int(input("enter the tenure in the years:  "))
score=int(input("enter the score out of 10: "))
if tenure <1 and score < 6:
    print("High risk ")
elif tenure <2  and score < 7:
    print("Medium risk ")
elif tenure >=2 and score >=8:
    print("low risk")
else:
    print("moderate risk")



credit_score= int(input("enter credit score "))
monthly_income= float(input("enter the monthly income"))
if credit_score >=750 and monthly_income >=50000:
    status =("Eligible for Premium Loan ")
elif credit_score >=700 and monthly_income >=35000:
    status =("Eligible for standard Loan ")
elif credit_score >=650 and monthly_income >=25000:
    status =("Eligible for Basic Loan ")
else:
    status =("not Eligible")
print("loan Status ",status)




#program to print no. from 0 to 10
for i in range(10):
    print(i)


for i in range(50,61):
    print(i)
#print no. from 5 to 1
for i in range(5,0,-1):
    print(i)
#print no. from 69 to 63     
for i in range(69,62,-1):
    print(i)
#print odd no.
for i in range(1,11,2):
    print(i)

#print even no. from 20 to 40
for i in range(20,41,2):
    print(i)
#print series 1,4,7,10,13,16
for i in range(1,18,3):
    print(i)
#print odd no. from 9 to 1
for i in range(9,0,-2): #yaha humne -2 isliye liya ki reverse krre but 2 step lena hai isliye
     print(i)
    
#accept a number anf print table of a number
num = int(input("enter the number here "))
for i in range(1,11):
    print(num,"*",i ,"=", num*i)
#accept the number and print factorial of a number
num =int(input("enter the number : "))
fact = 1
for i in range(1,num+1):
   fact = fact * i# 1*1=1, 1*2=2,2*3=6,6*4=24,24*5=120
print("factorial",fact)



#accept atm pin (give 3 attempt chack with fixed pi(1234)

istrue = False
for i in range(3):
    pin=int(input("enter the pin no.:")) 
    if pin==1234:
        print("succesfully proceed with transactions") 
        istrue = True
        break
    else:
        print("invalid pin,try again")
if istrue == False :
    print("your 3 attempts are over , try after 24 hours ")
    




#accept internet data consumed by the user for eax=ch session

dataconsumed = int(input("enter data consumed in mb "))
totaldata = 500

totaldata = totaldata-dataconsumed
if totaldata <= 0:
    print("total data exhausted,no internet")
elif totaldata <=100:
    print("low data,it will sooon expire")
else:
    print("total balance",totaldata,"mb")


                                                                                                  
#resend otp
import time
otp = 12345
for i in range(5,0,-1):
    print("you otp :",otp,"is valid for ",i,"seconds")
    time.sleep(1) # 1 seconds ke liye rukega program 
print("now you can click on resend otp button ")



#you are depositing balance amount 10000 with 10% annual rate for 3 years

#display how much amount will be year wise for 3 years
balance = 10000
rate = 0.10

for i in range(1,4):
    balance =balance+(  balance * rate)
    print("amount for year : ", i , " is ", balance)
print("total amount after 3 years ", balance)



#accept atm pin for 3 times


for i in range(3):
    pin = int(input("enter the pin of your atm card :"))
    if pin == 1234:
        print("succesfully login")
        break 
    else:
        print("invalid pin")
    if i >1 :
        print("your 3 attempts are over now , try again later")



num=int (input("enter the number "))
for i in range (2,num):
    if num % i==0:
        print("not prime number")
        break
if num == i+1:
    print("number is prime number ")
         


# accept the number from the user and print the factorial of the number
numa= int (input("enter the number"))
factorial = 1
for i in range(1,numa +1):
    factorial = (factorial * i )
print(factorial)



num= int(input("enter the number"))
factorial=1
for i in range(num, 0, -1):
    factorial*= i
    
print(factorial)



#accept cosprice and selling price
cp = float (input("enter the cost price: ")) #150
sp = float (input("enter the selling  price: ")) #230
amount = sp - cp
if amount >0:
    print("profi: ",amount)
elif amount < 0:
    print("loss :",-(amount))
else:
    print("no loss and no profit ")


#accept traffic signal colour
colour = input("enter the trafic signal colour ").lower()
if colour == "red":
    print ("please stop")
elif colour == "green":
    print("let's go")
elif colour == "yellow":
    print("ready to go")
else:
    print("invalid colour")


#accept the order_status ( processed, shipped ,delivered ) and then print relevant status
order_status = input("order_status ( processed, shipped ,delivered ): ")
if order_status == "processed":
    print("order is packed and ready to dispatch ")
elif order_status == "shipped":
    print("shipped , on the way ")
elif order_status == "delivered":
    print("delivered to customer successfully")
else:
    print("invalid order status ")



#accept age and fare (toatal fare = 0 fro age < =5, and 50 % off for age greater than 65
age = int(input("enter age :"))
if age <= 5 :
    print("fare is free")
else :
    fare = float(input("enter the fare "))
    if age >= 65:
        print("total fare is ",fare*0.5)
    else:
        print("fare is ",fare)


#accept init_bal , amount ,and transaction_type (deposit and withdrawl)
init_bal = int(input("enter the intial balnace :"))
amount = int(input("enter the amount : "))
trans_type= input("enter deposit or withdrawl :")
if trans_type == "deposit":
    init_bal = init_bal + amount
elif trans_type == "withdrawl":
    init_bal = init_bal - amount
else:
    print("invalid transaction type")
print("balance is ",init_bal)

num = int(input("enter the number here z:"))
fact = 1
for i in range (1,num+1):
    fact= (fact *i)
    
    print(fact)




