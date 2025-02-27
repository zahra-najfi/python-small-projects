num=(float(input("Enter a number:")))
temp=num
rev=0
while temp > 0:
    digit=temp%10
    rev=rev*10 + digit
    temp=temp//10


if num==rev:
    print(f"Number is a palindrome {num}")

else:
     print(f"Number is  not a palindrome {num}")

    
