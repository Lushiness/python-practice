#Compute factorial using a loop. 
def factorial() : #defining a function called factorial
    y=int(input("Enter a number: ")) #declaring a variable y for storing the number inputed
    ans = 1 #setting multiplication from 1
    if y==0: #
        print("factorial is 1") #print 1 if y is 0
    else:
        for i in range (1,y+1): #creates a loop between 1 and y ie range() stops before the number y+1
            ans *= i #ans = ans * i
        print("The factorial is " +  str(ans)) # prints the statement and changes ans to a string
factorial()#calling the function

