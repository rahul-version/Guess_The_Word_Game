import random as rd   # Using Random for Chossing Random number 
 
def game():
    # lst of Word 
    lst1 =['Apple','Beach','Brain','Bread','Brush','Chair','Chest','Chord','Click','Clock','Cloud','Dance','Diary'
           ,'Drink','Earth','Fruit','Ghost','Grape','Green','Happy','Heart','House','Juice','Light','Money',
           'Music','Party','Pizza','Plant','Radio','River','Salad','Sheep','Shoes','Smile','Snack', "Snake","Spice",
           "Spoon","Storm","Table","Toast","Tiger","Train","Water","Whale","Wheel","Woman","World","Write"]
    correct_index =[]   #Using list For storing Correct index 
    incorrect_index = []  #Using list for storing Incoort index
    n = rd.randint(0,len(lst1)-1)   # Choosing random number from Range(0, len(lst)-1)
    word = lst1[n]    # Taking the Word form lst For Guessing!!!!
    total_tries = 6      # Number of Tries
    tries = 1             
    print("Welcome To The Game Of Guessing The Word,Try Your Luck")   # Greeting!!!
    while tries <= total_tries:           #Using While Loop
        guess = input("Enter the Guessing Word :").capitalize()
        if len(guess) != len(word):            #Checking length
            print("Invalid Length of World")
            tries +=1                     # Incrementing tries
        if guess == word :                # IF you Guess Correct
            print("                  $$$    Congratulations You Won The Game    $$$                  ")
            break
        else:
            print("<< Try Again >>","        ","Tries Left: ",6 - tries)       # Printing Tries Left
            tries +=1
        for i in range(len(word)):                # Using for Loop for Simplicity
            if guess[i] == word[i]:
                correct_index.append(i)
            elif guess[i] in word and guess[i] != word[i]:
                incorrect_index.append(i)
        correct_string = "".join([guess[i] if i in correct_index else "-" for i in range(len(guess))])
        for i in incorrect_index:
            lst =[]
            lst.append(guess[i])
            print("Letter Exist: ", lst)             # Printing the Letter Exist
        print( "Correct String: ", correct_string)   # Printing the Partial string 
        
        print("correct position: ", correct_index)    # Printing the Correct index position
        print("incorrect position: ", incorrect_index)    # Printing the Incorrect Index position 
        
        correct_index.clear()
        incorrect_index.clear()
        
        if tries == total_tries and guess != word:           # If Tries Over ,Game Over
            print("                ###    Game Over YOU LOSt    ###             ")
game()