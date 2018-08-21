# Returns true if m is prime else false
def prime(m):
    return all([(m % j) for j in range(2, int(m**0.5)+1)]) and m>1
 
# Driver code
m = 41
if prime(m):
       print("Yes")
else:
    print("No")
