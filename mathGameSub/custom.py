def easyMode(number_of_questions):
    """
    A function to allow user to play a custom game in easy mode.
    Generates two random operands within the range 0 to 10.
    Only addition operator is used.
    Generates requested number of questions by the user.
    
    Arguments :
    number_of_questions - requested number of questions by the user.
    """
    
    import random
    global results, count
    
    print()
    print("Easy Mode".center(29))
    print("-" * 29)
    print()
    
    results = []
    count = 0
    
    #Generating questions with random operands
    for i in range (1, (number_of_questions+1)):
        operand1 = random.randrange(0, 11)
        operand2 = random.randrange(0, 11)
        
        real_answer = operand1 + operand2
        
        question = f"{i:2}) {operand1:2} + {operand2:2}  = "
        user_answer = input(question)
        
        #Checking if the user's answer is correct or incorrect and appending the questions and answers in to the resulsts list
        if (real_answer == int(user_answer)):
            results.append(f"{question} {user_answer:2} (Answer is {real_answer:2}) [Correct]")
            count += 1
        else:
            results.append(f"{question} {user_answer:2} (Answer is {real_answer:2}) [Incorrect]")

def mediumMode(number_of_questions):
    """
    A function to allow user to play a custom game in medium mode.
    Generates two random operands within the range 0 to 50.
    Addition or Subtraction operator will be randomly generated.
    Generates requested number of questions by the user.

    Arguments :
    number_of_questions - requested number of questions by the user.
    """
    
    import random
    global results, count

    print()
    print("Medium Mode".center(29))
    print("-" * 29)
    print()
    
    results = []
    count = 0
    operators = ["+", "-"]
    
    #Generating questions with random operands and operators
    for i in range (1, (number_of_questions + 1)):
        operand1 = random.randrange(0, 51)
        operand2 = random.randrange(0, 51)
        operator = random.choice(operators)
        
        real_answer = eval(str(operand1) + operator + str(operand2))
        
        question = f"{i:2}) {operand1:2} {operator} {operand2:2}  = "
        user_answer = input(question)
        
        #Checking if the user's answer is correct or incorrect and appending the questions and answers in to the empty list
        if (int(real_answer) == int(user_answer)):
            results.append(f"{question} {user_answer:3} (Answer is {real_answer:3}) [Correct]")
            count += 1
        else:
            results.append(f"{question} {user_answer:3} (Answer is {real_answer:3}) [Incorrect]")

#Creating easy mode function
def hardMode(number_of_questions):
    """
    A function to allow user to play a custom game in hard mode.
    Generates two random operands within the range 0 to 100.
    Addition or Subtraction or Multiplication operator will be randomly generated.
    Generates requested number of questions by the user.

    Arguments :
    number_of_questions - requested number of questions by the user.
    """
    
    import random
    global results, count

    print()
    print("Hard Mode".center(29))
    print("-" * 29)
    print()

    results = []
    count = 0
    operators = ["+", "-", "*"]
    
    #Generating questions with random operands and operators
    for i in range (1, (number_of_questions + 1)):
        operand1 = random.randrange(0, 101)
        operand2 = random.randrange(0, 101)
        operator = random.choice(operators)
        
        real_answer = eval(str(operand1) + operator + str(operand2))
        
        question = f"{i:2}) {operand1:3} {operator} {operand2:3}  = "
        user_answer = input(question)
        
        #Checking if the user's answer is correct or incorrect and appending the questions and answers in to the empty list
        if (int(real_answer) == int(user_answer)):
            results.append(f"{question} {user_answer:5} (Answer is {real_answer:5}) [Correct]")
            count += 1
        else:
            results.append(f"{question} {user_answer:5} (Answer is {real_answer:5}) [Incorrect]")

def displayResults(name, difficulty, number_of_questions):
    """
    A function to display the gameplay results.

    Arguments :
    name - Name of the user.
    difficulty - difficulty mode requested by the user.
    number_of_questions - requested number of questions by the user.
    """
    
    import mysql.connector
    
    percentage = (count / number_of_questions) * 100

    #Printing game results
    print()
    print("-" * 29)
    print("Game Results".center(29))
    print("-" * 29)

    print("\nYour name is", name)
    print("You Played a Custom Game in " + difficulty + " Mode")
    print("You Have Answered", number_of_questions, "Questions")
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
    mySQLText = "INSERT INTO tbl_past_player_results (name,correct,total,percentage) VALUES(%s, %s, %s, %s)"
    myValues = (name, count, number_of_questions, "{:0.1f}" . format(percentage) + "%")
    
    cursor.execute(mySQLText, myValues)
    db.commit()
    db.close()
    
    #Initializing a loop to iterate until user press enter key to go back to game menu
    while True:
        go_back = input("\nPress enter to go back to Game Menu : ")
        if (go_back == ""):
            break
    
