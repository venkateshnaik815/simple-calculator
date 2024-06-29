def calculator():
   print("simple calculator")
   print("1. addition")
   print("2.subtraction")
   print("3. multiplication")
   print("4. devision")

while True:
 choice =   (input("enter a chioce(1/2/3/4): "))
    
if choice in ['1','2','3','4']:
    num1 = float(input("Enter a first number:"))

    num2 = float(input("enter a second number:"))

if choice == "1":
   print(num1 , "+" , num2, "=", num1+num2)

elif choice == "2":
    print(num1 ,"-", num2,   "=" ,num1-num2)

elif choice == "3":
   print(num1 , "*" ,num2, "=" ,num1*num2)
elif choice == "4":
   print(num1,"/" , num2 ,"=",num1/num2 )
else :
   print("invalid input")
    





   

