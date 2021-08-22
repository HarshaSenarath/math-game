# Mathematics Game

### Description

This application was developed as a part of my foundation certificate program.
This is a command console application which will allow user to play a simple mathematics game.
The game has two types of game plays which are quick gameplay and custom gameplay.
Quick gameplay will genearte five addtion questions with random operands within the range 0 to 10.
Custom gameplay will have three difficulties which will have alterations for each difficulty as below.


| Difficulty | Operators Used | Operand Range | Sample                          | No of Questions   |
| -----------| -------------- | ------------- | ------------------------------- | ----------------- |
| Easy       | +              | 0 to 10       | 7 + 3                           | Player can decide |
| Medium     | + and -        | 0 to 50       | 32 - 5 <br> 25 + 22             | Player can decide |
| Hard       | +, - and *     | 0 to 100      | 5 - 15 <br> 35 + 68 <br> 78 * 5 | Player can decide |


Results of each gameplay will be displayed at the end of each play.
The results will also be saved inside a database and past gameplay results can be viewed as well.

###### Technologies

  * Python

### How to Use

xampp and mysql connector will be required inorder for this program to work and the attached database must be imported.

###### Installation

` pip install mysql-connector-python `
