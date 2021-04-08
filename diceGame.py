import random
from graphics import *
import time

'''
Ayesha Siddiqua
3/5/2020
'''

# Getting dice number
def rollDice():
    return random.randint(1, 6)

#Creating dice illustration based on dice number
def dice_picture(dice):

    zero   = ""
    one    = "         \n         \n    o    \n         \n         "
    two    = "         \n  o      \n         \n      o  \n         "
    three  = "         \n   o     \n    o    \n     o   \n         "
    four   = "         \n   o o   \n         \n   o o   \n         "
    five   = "         \n   o o   \n    o    \n   o o   \n         "
    six    = "         \n   o o   \n   o o   \n   o o   \n         "

    if dice == 0:
        return zero
    elif dice == 1:
        return one
    elif dice == 2:
        return two
    elif dice == 3:
        return three
    elif dice == 4:
        return four
    elif dice == 5:
        return five
    elif dice == 6:
        return six
        
user_score = 0
computer_score = 0

# Creating window
win = GraphWin("Dice Game", 900, 900)
win.setCoords(0,0,10,10)

#Creating the Welcome box outline
welcomeBox = Rectangle(Point(3, 3), Point(7, 7))
welcomeBox.draw(win)

# Creating welcome title
welcomeTitle = Text(Point(5, 6), "Welcome to the Dice Game")
welcomeTitle.draw(win)

# Getting player name from user
enterNameText = Text(Point(5,5), "Enter your name below. \nClick the Enter button to start the game!")
enterNameText.draw(win)

textEntry = Entry(Point(5, 4.25), 15)
textEntry.draw(win)

# Creating enter button
enterBox = Rectangle(Point(4.5, 3.25), Point(5.5, 3.75))
enterBox.setFill("green")
enterBox.draw(win)
enterBoxText = Text(Point(5, 3.5), "Enter")
enterBoxText.draw(win)

enterBox_x1 = enterBox.getP1().getX()
enterBox_y1 = enterBox.getP1().getY()
enterBox_x2 = enterBox.getP2().getX()
enterBox_y2 = enterBox.getP2().getY()

clickInsideButton = False
while(clickInsideButton == False):
    click = win.getMouse()

    if( (click.getX() >= enterBox_x1) and (click.getX() <= enterBox_x2) and (click.getY() >= enterBox_y1) and (click.getY() <= enterBox_y2) ):
        enterBoxText.setStyle("bold")
        clickInsideButton = True
        user_name = textEntry.getText()                

# Going to game screen
welcomeBox.undraw()
welcomeTitle.undraw()
enterNameText.undraw()
textEntry.undraw()
enterBox.undraw()
enterBoxText.undraw()

# Creating game screen title
title = Text(Point(5,9.5), "Dice Game")
title.draw(win)

#Displaying instructions
instructions = Text(Point(5,9), "HOW TO PLAY: Roll the die to increase your score or pass your turn to keep your points so far.\nIf the dice is 1, your points from the round are 0. Win by beating the computer to a 100 score!" )
instructions.draw(win)

# Creating player 1 box and text
Player1NameBox = Rectangle(Point(1.5, 7.5), Point(4.5, 8.5))
Player1NameBox.draw(win)
Player1Text = Text(Point(3, 8), "Player 1\n"+user_name)
Player1Text.draw(win)

# Creating computer box and text
Player2NameBox = Rectangle(Point(5.5, 7.5), Point(8.5, 8.5))
Player2NameBox.draw(win)
Player2Text = Text(Point(7, 8), "Player 2\nComputer")
Player2Text.draw(win)

# Creating player 1 score box
Player1ScoreBox = Rectangle(Point(2, 6), Point(4, 7))
Player1ScoreBox.draw(win)
Player1ScoreText = Text(Point(3, 6.5), user_score )
Player1ScoreText.draw(win)

# Creating computer score box
Player2ScoreBox = Rectangle(Point(6, 6), Point(8, 7))
Player2ScoreBox.draw(win)
Player2ScoreText = Text(Point(7, 6.5), computer_score)
Player2ScoreText.draw(win)

# Creating temp score box
TemporaryScoreBox = Rectangle(Point(4.5, 5), Point(5.5, 6))
TemporaryScoreBox.draw(win)
TemporaryScoreText = Text(Point(5, 5.5), 0)
TemporaryScoreText.draw(win)

# Creating text to display turn
whoPlayingText = Text(Point(5, 4.5), user_name + " Playing")
whoPlayingText.draw(win)

# Creating text to display choice
playerBottonChosen = Text(Point(5, 4), "Please choose a button: ")
playerBottonChosen.draw(win)

# Creating dice
dice = Rectangle(Point(4.5, 2), Point(5.5, 3))
dice.draw(win)
diceText = Text(Point(5, 2.5), dice_picture(0))
diceText.draw(win)

# Creating the "Roll Dice" button and text
rollDiceButton = Rectangle(Point(2, 1), Point(4, 2))
rollDiceButton.draw(win)
rollDiceButtonText = Text(Point(3, 1.5), "Roll Dice")
rollDiceButtonText.draw(win)

# Creating the "Pass Turn" button and text
PassTurnButton = Rectangle(Point(6, 1), Point(8, 2))
PassTurnButton.draw(win)
PassTurnButtonText = Text(Point(7, 1.5), "Pass Turn")
PassTurnButtonText.draw(win)

# Obtaining coordinates of button
rollDiceButton_x1 = rollDiceButton.getP1().getX()
rollDiceButton_y1 = rollDiceButton.getP1().getY()
rollDiceButton_x2 = rollDiceButton.getP2().getX()
rollDiceButton_y2 = rollDiceButton.getP2().getY()

passButton_x1 = PassTurnButton.getP1().getX()
passButton_y1 = PassTurnButton.getP1().getY()
passButton_x2 = PassTurnButton.getP2().getX()
passButton_y2 = PassTurnButton.getP2().getY()


while user_score < 100 and computer_score < 100:
    
    amount_added = 0 # variable to hold temp score

    # Loop for player
    while True:

        # Highlighting to identify current player
        Player1NameBox.setFill("green")
        whoPlayingText.setText(user_name + " Playing")

        clickInsideButton = False      
        # looping to click a button
        while(clickInsideButton == False):
            click = win.getMouse()

            #if statements to see which button user clicked ..   
            if( (click.getX() >= rollDiceButton_x1) and (click.getX() <= rollDiceButton_x2) and (click.getY() >= rollDiceButton_y1) and (click.getY() <= rollDiceButton_y2) ):
                clickInsideButton = True
                rollDiceButtonText.setStyle("bold")
                rollDiceButtonText.setStyle("normal")
                selection = 1

            if( (click.getX() >= passButton_x1) and (click.getX() <= passButton_x2) and (click.getY() >= passButton_y1) and (click.getY() <= passButton_y2) ):
                clickInsideButton = True
                PassTurnButtonText.setStyle("bold")
                PassTurnButtonText.setStyle("normal")
                selection = 2

        #if user clicks "Roll Button"        
        if selection == 1:
            dice = rollDice()
            playerBottonChosen.setText(user_name + ' chose "Roll Dice" button and got a ' + str(dice))
            diceText.setText(dice_picture(dice))
            
            #if dice is 1, do not add to user_score and make temporary box score 0  
            if dice == 1:
                TemporaryScoreText.setText(0)
                amount_added = 0
                Player1NameBox.setFill("white")
                time.sleep(3)
                break
            else:
                # dice is not 1 and so add to the temporary score box
                amount_added += dice
                TemporaryScoreText.setText(amount_added)
  
        #if user clicks "Pass Turn" 
        if selection == 2:
            playerBottonChosen.setText(user_name + ' chose "Pass Turn" button')
            #add the amount_added value gathered so far into our Player's score box
            Player1ScoreText.setText( user_score + amount_added )
            
            user_score += amount_added
            amount_added = 0
            TemporaryScoreText.setText(0)
            
            time.sleep(3) 
            Player1NameBox.setFill("white")
            break

    #if user_score after rolling(s) is greater than or equal to 100, break out of "outer" while loop
    if (user_score >= 100):
        break  
                
    # Loop for computer
    while True:

        #Highlighting to identify current player
        Player2NameBox.setFill("green")
        whoPlayingText.setText("Computer Playing")

        #generating random number to decide if computer rolls or passes
        computerRandom = random.randint(1, 2)

        #if computer is doing "Roll Button"
        if computerRandom == 1:
            rollDiceButtonText.setStyle("bold")
            rollDiceButtonText.setStyle("normal")
            
            dice = rollDice()
            playerBottonChosen.setText('Computer chose "Roll Dice" button and got a ' + str(dice))
            diceText.setText(dice_picture(dice))

            #if dice is 1, do not add to computer_score and make temporary box score 0
            if dice == 1:
                TemporaryScoreText.setText(0)
                amount_added = 0
                Player2NameBox.setFill("white")
                time.sleep(3)
                playerBottonChosen.setText('Please choose a button: ')  
                break
            else:
                # dice is not 1 and so add to the temporary score box
                amount_added += dice
                TemporaryScoreText.setText(amount_added)

            time.sleep(3)    

        #if computer is doing "Pass Turn"
        if computerRandom == 2:
            PassTurnButtonText.setStyle("bold")
            PassTurnButtonText.setStyle("normal")

            #added_amount is added to computer score
            playerBottonChosen.setText('Computer chose "Pass Turn" button')
            Player2ScoreText.setText( computer_score + amount_added )
            
            computer_score += amount_added
            amount_added = 0
            TemporaryScoreText.setText(0)

            time.sleep(3)
            Player2NameBox.setFill("white")
            playerBottonChosen.setText('Please choose a button: ')
            break

    #if computer_score after rolling(s) is greater than or equal to 100, break out of "outer" while loop
    if(computer_score >= 100):
            break

# Creating a filled white rectangle to place winner info
declareWinnerBox = Rectangle(Point(0, 0), Point(10, 7))
declareWinnerBox.setFill("white")
declareWinnerBox.draw(win)

#Create text placeholder to put in winner info
declareWinnerBoxText = Text(Point(5, 5.5), "")
declareWinnerBoxText.draw(win)

#Text to display if user wins or computer wins
if user_score >= 100:
    declareWinnerBoxText.setText(user_name + " won with " + str(user_score) + " points!\nCongratulations!!")

if computer_score >= 100:
    declareWinnerBoxText.setText("Sorry, Computer won with " + str(computer_score) + " points")
