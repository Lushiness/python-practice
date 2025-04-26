#Factorial (Recursive)
def factorial(num): #defining a function factorial that takes a parameter num
    if num == 0: 
        return 1 # if the number entered is 0 the number one is returned as the output
    else:
        return num * factorial(num-1) # linear recursion where the function is called again
    
num  =int(input("Enter a number: ")) #prompts the user to enter a number
ans = factorial(num) # a variable called num which stores the answer
print("The factorial is ", str(ans)) # printing the answer
