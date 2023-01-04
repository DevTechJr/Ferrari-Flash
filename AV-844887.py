'''
Name : Anirudh Bharadwaj Vangara 844887

Program Title : Mario Math Time

Program Description : A math flash cards game to help students practice math
                      with Mario and Luigi!
'''
# Import Libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random

#Define Functions

# checkInput function
# Inputs : None
# Results : None
def checkInput():

    # Import Global Variables
    global maxNum # Maximum Number
    global boolNegativeNums # Boolean Value for Negative Numbers
    global boolModulus # Boolean Value for Modulus Operator
    global correctCount # Number of Correct Attempts
    global wrongCount # Number of Wrong Attempts
    global totalCount # Number of Total Attempts
    global systemLog # System Message Log Interface

    boolNegativeNums = inclNegativeNums.get() # Reassign boolNegativeNums value based on User Input
    boolModulus = inclModulus.get() # Reassign boolModulus value based on User Input
    levelSelection = combo.get() # Capture combobox input and store to levelSelection variable
    if levelSelection not in combo["values"]:
        # Invalid Level Selected
        systemLog.config(text="Invalid Level Selected! Try Again!")
    else:
        try:
            # Further validate input
            if levelSelection == "Level 1 (1-3)":
                frame1.config(bg="green") # Change frame background
                maxNum = 3 # Reassign maximum number value
            elif levelSelection == "Level 2 (1-6)":
                frame1.config(bg="yellow") # Change frame background
                maxNum = 6 # Reassign maximum number value
            elif levelSelection == "Level 3 (1-9)":
                frame1.config(bg="orange") # Change frame background
                maxNum = 9 # Reassign maximum number value
            elif levelSelection == "Level 4 (1-12)":
                frame1.config(bg="red") # Change frame background
                maxNum = 12 # Reassign maximum number value
            systemLog.config(text="(System Log Messages)") # Reset System Log

            # Reset All Game Counter Values
            totalCount = 0
            correctCount = 0
            wrongCount = 0
            # Reset Game Counter Value Displays
            numCorrect_value.config(text=correctCount)
            numTotal_value.config(text=totalCount)
            numWrong_value.config(text=wrongCount)
            systemLog.config(text="Game has started!") # Game has started message
            gen_question() # Invoke gen_question function to initially start
        except:
            systemLog.config(text="Error in validating input! Try Again!")

def gen_question():
    # Import Global Variables
    global boolModulus
    global operators
    global maxNum
    global boolNegativeNums
    global num1
    global num2
    global expression
    global leastNum
    global answer

    if boolModulus: 
        # If user selected modulus operator, add it into operators list
        operators.append("%")
    
    if boolNegativeNums:
        # Least Number = Negative Maximum Number
        leastNum = 0-maxNum
    else:
        # Least Number = 1
        leastNum = 1
    
    # Generate random numbers and assign them to variables
    num1 = random.randint(leastNum,maxNum)
    num2 = random.randint(leastNum,maxNum)

    # Generate random operator and assign it to variable
    operator = random.choice(operators)

    # Generate expression, assign it to variable and display it
    expression = f"{num1} {operator} {num2}"
    questionDisplay.config(text=expression)

    # Generate answer and assign it to variable
    answer = float(eval(f"{num1} {operator} {num2}"))

def resetValue():
    # Import Global Variables
    global correctCount
    global wrongCount
    global totalCount
    global systemLog
    global pastQuestion

    # Reset Game Counters
    totalCount = 0
    correctCount = 0
    wrongCount = 0

    # Display Game Counters (after reset)
    numCorrect_value.config(text=correctCount)
    numTotal_value.config(text=totalCount)
    numWrong_value.config(text=wrongCount)

    # Reset frame 1 background color
    frame1.config(bg="blue")

    # Reset question display
    questionDisplay.config(text="")

    # Empty questionInput entry
    questionInput.delete(0, 'end')

    # Log game reset message
    systemLog.config(text="Game has been reset")

    # Reset past question
    pastQuestion.config(text="")

def updateScore():
    # Import Global Variables
    global correctCount
    global wrongCount
    global totalCount

    # Update displays of game counters
    numCorrect_value.config(text=correctCount)
    numTotal_value.config(text=totalCount)
    numWrong_value.config(text=wrongCount)

def checkAnswer():
    # Import Global Variables
    global correctCount
    global wrongCount
    global totalCount
    global pastQuestion

    # Try to get user given answer
    try:
        # Use float to accommodate possible decimal values
        attempt = float(questionInput.get())
    except:
        # Due to bad input, update attempt value to ""
        attempt = ""
    
    # If answer is correct :
    if answer == attempt:

        # Update counters
        correctCount+=1
        totalCount+=1

        # Update score and display question as past question
        updateScore()
        pastQuestionMessage = f"Past Question :   {expression} = {questionInput.get()} (Correct Answer)"
        pastQuestion.config(text=pastQuestionMessage)
    else:
        # Update counters
        wrongCount+=1
        totalCount+=1

        # Update score and display question as past question
        updateScore()
        pastQuestionMessage = f"Past Question :   {expression} = {questionInput.get()} (Correct Answer = {answer})"
        pastQuestion.config(text=pastQuestionMessage)
    
    # Empty questionInput entry
    questionInput.delete(0, 'end')

    # Generate next question
    gen_question()

# Define global variables
num1 = 0 # Random number 1
num2 = 0 # Random number 2
operators = ["*","+","-"] # Initial operators
expression = "" # Expression string
answer = "" # Answer to expression

maxNum = 0 # Maximum possible value for random number
leastNum = 1 # Least possible value for random number
boolNegativeNums = False # Boolean value for negative numbers
boolModulus = False # Boolean value for modulus

correctCount = 0 # Number of correct attempts
wrongCount = 0 # Number of wrong attempts
totalCount = 0 # Number of total attempts

# Create Tkinter Window
window = tk.Tk()
window.title("Mario Math Time!")
window.geometry("640x290")

# Define 2 sides of app
frame1 = tk.Frame(window) # App left side
frame1.config(bg="blue")
frame1.grid(row=0, column=0,sticky="ns")

frame2 = tk.Frame(window) # App right side
frame2.config(bg="red")
frame2.grid(row=0, column=1,sticky="ns")

# Frame 2 Components

# App heading
appLabel = tk.Label(frame2, text="MARIO MATH TIME")
appLabel.grid(column=0, row=0, padx=6, pady=6)

# App options
optionsFrame = tk.Frame(frame2)
optionsFrame.grid(row=1, column=0,padx=3, pady=3)

# Declare Options Variables
inclNegativeNums = BooleanVar()
inclModulus = BooleanVar()

# Negative Number Checkbox
checkNegativeNums = Checkbutton(optionsFrame, text = "Include Negative Numbers",variable=inclNegativeNums)
checkNegativeNums.grid(column=0,row=1,sticky = "NESW")

# Modulus Button Checkbox
checkModulus = Checkbutton(optionsFrame, text = "Include Modulus Operator",variable=inclModulus)
checkModulus.grid(column=0,row=2)

# Create Combobox for level selection
combo_label = Label(optionsFrame, text="Pick A Level :")
combo_label.grid(column=0,row=3,sticky = "w" )
combo = ttk.Combobox(optionsFrame)
combo['values'] = ["Level 1 (1-3)","Level 2 (1-6)","Level 3 (1-9)","Level 4 (1-12)"] # Level options
combo.current(0) # Set the selected item to level 1
combo.grid(row=3, column = 1)

# Button to submit game options
submitOptionsBtn = tk.Button(optionsFrame,text="Start Game",fg='white',command=checkInput)
submitOptionsBtn.config(bg="green")
submitOptionsBtn.grid(row=5,column=0,columnspan=2, sticky='ew',pady=10,padx=10)

# Button to reset game
resetBtn = tk.Button(optionsFrame,text="Reset Game",fg='red',command=resetValue)
resetBtn.config(bg="yellow")
resetBtn.grid(row=6,column=0,columnspan=2,sticky='ew',pady=10,padx=10)

# System Message Log widget to display game messages
systemLog = tk.Label(optionsFrame,text="(System Log Messages)")
systemLog.grid(row=7,column=0, columnspan=2, sticky='ew',padx=10,pady=10)

# Widget to display past question attempted by user
pastQuestion = tk.Label(optionsFrame,text="")
pastQuestion.grid(row=8,column=0, columnspan=2, sticky='ew',padx=10,pady=10)

#Frame 1 Components
consoleFrame = tk.Frame(frame1) # Console frame to show question and accept answer
consoleFrame.config(bg="red")
consoleFrame.grid(row=1, column=1,padx=10,pady=10)

# Mario Jumping picture
img1 = PhotoImage(file='marioJump.png')
lbl1 = Label( frame1, image = img1)
lbl1.grid(row=0, column=1,sticky="w",padx=5,pady=5)

# Luigi Jumping picture
img2 = PhotoImage(file='luigiJump.png')
lbl2 = Label( frame1, image = img2)
lbl2.grid(row=0, column=1,sticky="e",padx=5,pady=5)

# Display expression for user to attempt
questionDisplay = Label(consoleFrame,text="") # Set intial text to ""
questionDisplay.grid(row=1,column=1,padx=10,pady=10)

# Accept user input to displayed expression
questionInput = Entry(consoleFrame)
questionInput.grid(row=1,column=2,padx=5,pady=10)

# Button to validate user input and check it
checkAnswerBtn = tk.Button(consoleFrame,text="Check Answer",fg='white',command=checkAnswer)
checkAnswerBtn.config(bg="green")
checkAnswerBtn.grid(row=2,column=1,padx=5,pady=5,sticky="ew",columnspan=2)

# A frame widget to display game counters
countFrame = tk.Frame(frame1)
countFrame.config(bg="red")
countFrame.grid(row=2, column=1,padx=10,pady=10)

# Label for correct attempts game counter
numCorrect_label = Label(countFrame, text="Correct Attempts")
numCorrect_label.grid(row=2,column=1,padx=5,pady=5)

# Label for wrong attempts game counter
numWrong_label = Label(countFrame, text="Wrong Attempts")
numWrong_label.grid(row=2,column=2,padx=5,pady=5)

# Label for total attempts game counter
numLeft_label = Label(countFrame, text="Total Attempts")
numLeft_label.grid(row=2,column=3,padx=5,pady=5)

# Value display for correct attempts game counter
numCorrect_value = Label(countFrame, text="")
numCorrect_value.grid(row=1,column=1,padx=5,pady=5)

# Value display for wrong attempts game counter
numWrong_value = Label(countFrame, text="")
numWrong_value.grid(row=1,column=2,padx=5,pady=5)

# Value display for total attempts game counter
numTotal_value = Label(countFrame, text="")
numTotal_value.grid(row=1,column=3,padx=5,pady=5)

# To run app
tk.mainloop()