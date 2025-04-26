#Reverse a string (without using [::-1] or built-in methods).
def reverse_string(): # declaring a function called reverse_string
    text=input("Enter a word: ") # prompts the user to input a word
    reversed_text= " " # creates an empty string to store the reversed text

    for char in text : # for each character in the inputed text 
        reversed_text = char + reversed_text #adds the character before not after
    print("The reversed text is: " , reversed_text) #prints the reversed_text

reverse_string()#calls the function