#Creating quick game function
def quickGameplay():
    """
    A function to allow user to play a quick game.
    Generates two random operands within the range 0 to 10.
    Only addition operator is used.
    Generates 5 questions.
    Displays gameplay results at the end.
    """
    
    import random
    import mysql.connector
    
    results = []
    count = 0

    print()
    print("-" * 29)
    print("Quick Game Play".center(29))
    print("-" * 29)
    
    name = input("\nEnter Your Name : ")
    print()
    
    #Generating questions with random operands
    for i in range (1,6):
        operand1 = random.randrange(0,11)
        operand2 = random.randrange(0,11)
        
        real_answer = operand1 + operand2

        question = f"{i}) {operand1:2} + {operand2:2}  = "
        user_answer = input(question)
        
        #Checking if the user's answer is correct or incorrect and appending the questions and answers in to the resulsts list
        if (real_answer == int(user_answer)):
            results.append(f"{question} {user_answer:2} (Answer is {real_answer:2}) [Correct]")
            count += 1
        else:
            results.append(f"{question} {user_answer:2} (Answer is {real_answer:2}) [Incorrect]")
            
    percentage = (count / 5) * 100
    
    #Printing game results
    print()
    print("-" * 29)
    print("Game Results".center(29))
    print("-" * 29)
    
    print("\nYour Name is", name)
    print("You Played a Quick Game")
    print("You Have Answered 5 Questions")
    print("Number of Correct Answers are", count)
    print("Your Final Score is", "{:0.1f}" . format(percentage) + "%")
    print()
    
    #Printing questions and answers
    for j in results:
        print(j)
        
    #Connecting to the database
    conDict = {'host':'localhost',
             'database':'db_math_game',
             'user':'root',
             'password':''}
    
    db = mysql.connector.connect(**conDict)
    cursor = db.cursor()
    
    #Inserting values into the database
    mySQLText = "INSERT INTO tbl_past_player_results (name,correct,total,percentage) VALUES(%s,%s,%s,%s)"
    myValues = (name, count, "5", "{:0.1f}" . format(percentage) + "%")
    
    cursor.execute(mySQLText, myValues)
    
    db.commit()
    db.close()
    
    #Initializing a loop to iterate until user press enter key to go back to game menu
    while True:
        go_back = input("\nPress enter to go back to Game Menu : ")
        
        if (go_back == ""):
            break

    
    
