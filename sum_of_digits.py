#Sum of Digits of a Number 
def add(num): #decalring a function with a parameter num
    if num == 0 : #if num is 0 there is no sum
        return 0 # hence output is 0
    else :
        return num % 10 + add( num // 10) # the number is fetched and removed while being added
    
num = int(input("Enter a digit: ")) # prompts the user to enter a digit
ans = add(num) # the output is stored in a variable ans
print("The sum of the digits is: " , str(ans)) # outputs the answer