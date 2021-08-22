import mathGameSub.quick
import mathGameSub.custom
import sys
import mysql.connector
from mysql.connector import Error

#Handiling the errors which can occur when connecting to mysql connector
try:
    conn = mysql.connector.connect(host = 'localhost', user = 'root', password = '')
    
    if conn.is_connected():
        #Checking if the user entered last argument eqauls to "Start"
        if (sys.argv[-1].lower() == "start"):
            #Initializing a loop to iterate through the menu
            while True:
                print()
                print("-" * 29)
                print("Game Menu".center(29))
                print("-" * 29)
                print('''\n(1) Quick Game\
                         \n(2) Custom Game\
                         \n(3) Display Past Game Details\
                         \n(4) Exit''')
                
                #Initializing a loop to iterate until the user enters a valid option
                while True:          
                    menu_option = input("\nEnter your option : ")
                    
                    if (menu_option == "1"):
                        mathGameSub.quick.quickGameplay()
                        break
                    elif (menu_option=="2"):
                        print()
                        print("-" * 29)
                        print("Custom Game Play".center(29))
                        print("-" * 29)
                        
                        name = input("\nEnter Your Name : ")
                        
                        #Intitalizing a loop to iterate until user enters a valid difficulty level
                        while True:
                            difficulty = input("Select Your Difficulty Level (Type Easy, Medium or Hard) : ")
                            
                            if (difficulty.lower() == "easy"): 
                                number_of_questions = int(input("How Many Questions You Need : "))
                                mathGameSub.custom.easyMode(number_of_questions)
                                break
                            elif (difficulty.lower() == "medium"):
                                number_of_questions = int(input("How Many Questions You Need : "))
                                mathGameSub.custom.mediumMode(number_of_questions)
                                break
                            elif (difficulty.lower() == "hard"):
                                number_of_questions = int(input("How Many Questions You Need : "))
                                mathGameSub.custom.hardMode(number_of_questions)
                                break
                            else:
                                print("Invalid Difficulty Level")

                        mathGameSub.custom.displayResults(name, difficulty, number_of_questions)
                        break
                    elif (menu_option=="3"):
                        print()
                        print("-" * 80)
                        print("Past Player Results".center(80))
                        print("-" * 80)
                        print()

                        print("Name".center(20) + "Correct Answers".center(20) + "Total Questions".center(20) + "Percentage".center(20))

                        #Connecting to the database
                        conDict={'host':'localhost',
                                 'database':'db_math_game',
                                 'user':'root',
                                 'password':''}
                        
                        db = mysql.connector.connect(**conDict)
                        cursor = db.cursor()

                        #Fetching all the data in the database
                        cursor.execute("SELECT * FROM tbl_past_player_results")
                        data = cursor.fetchall()

                        #Printing all the data in the database
                        for item in data:
                            print()
                            for r in item:
                                print(str(r).center(20), end = "")
                        print()
                        
                        #Initializing a loop to iterate until user press enter key to go back to game menu
                        while True:
                            go_back = input("\nPress enter to go back to Game Menu : ")
                            if (go_back == ""):
                                break

                        break
                    elif (menu_option == "4"):
                        break
                    else:
                        print("Invalid input")
                if (menu_option == "4"):
                    break
        #Asking user to type "Start" as the last argument if he/she types something else
        else:
            print("Please type \"start\" at the end to play the game")
except Error as e:
    print(e)
    
    
