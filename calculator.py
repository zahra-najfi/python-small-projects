a = float(input("Enter the First Number: "))
b = float(input("Enter a Second Number: "))
operator=(input("Enter a operator(*,+,-,/,//,%):"))
#Conditions 
if operator == '*' :
    result=a*b
elif operator == '+':
    result=a+b 
elif operator == '-':
    result=a-b 
elif operator == '%':
    result=a%b if b!=0 else "Not module by zero"

elif operator == '/':
    result=a/b if b!=0 else "Not divided by zero"
elif operator == '//': 
    result=a//b if b!=0 else "Not divided by zero"
else :
    result= "invalid operator"        

print(result)    