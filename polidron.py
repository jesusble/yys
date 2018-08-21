num1 = int(input("enter a number: "))
 
temp1 = num1
rev1 = 0
 
while temp1 != 0:
    rev1 = (rev1 * 10) + (temp1 % 10)
    temp1 = temp1 // 10
 
if num1 == rev1:
    print("number is palindrome")
else:
    print("number is not palindrome")
