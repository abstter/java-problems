"""
Project: Flashcard Quiz App (Student Code)
Python Level 3
Chapter 18: File Handling

Student Name: Abhiram
Class Section: D14

Student Instructions:
---------------------
Fill in the missing code in this program to complete the flashcard app.
You will primarily be completing the file handling, question-and-answer
processing, and GUI setup.

Program Summary:
-----------------
This program creates a simple flashcard quiz application using tkinter for
the GUI. It loads a series of questions and their corresponding answers from a
text file, presents them to the user one at a time in a random order, and
allows the user to enter answers. The program tracks the number of correct
answers. At the end of the quiz, the user's name and score are saved to a
separate file, and all saved scores are displayed in a messagebox.
"""

import tkinter as tk
from tkinter import messagebox
import random


def load_questions(filename='questions.txt'):
    """
    Read questions and their answers from a specified file and load them
    into a list for later use.
    
    The function expects a file where each question is followed by its answer,
    with questions and answers on separate lines.
    
    Parameters:
    - filename: Path to the file containing questions and answers. Defaults to
      'questions.txt'.
    
    Returns:
    - A list of tuples, where each tuple contains a question and its answer.
    """
    ### Student Code [8 points -> 4 points per line]:
    # Open file filename for reading, read the contents into a list of strings,
    # and assign the variable lines to this list:
    question_list = []
    with open (filename, 'r') as questionsandanswers:
        questions_list = questionsandanswers.readlines()
        
    # Initialize an empty list to store question-answer pairs:
    questions_and_answers = []
    
    ### Student Code [16 points -> 4 points per line]:
    # Iterate through questions_list. Step by 2 to get question-answer pairs:
    for i in range(0, len(questions_list), 2):
        # Get the question from questions_list, remove leading/trailing
        # whitespace, and assign it to the variable question:
        question = questions_list[i].strip()
        # Get the corresponding answer, remove leading/trailing whitespace, and
        # assign it to the variable answer:
        answer = questions_list[i+1].strip()
        # Append the question-answer pair as a tuple to a list called
        # questions_and_answers:
        questions_and_answers.append((question, answer))
        
    
    # Return the completed list of the question-answer tuple pairs:
    return questions_and_answers


def save_and_display_scores(name, score):
    """
    Save the user's score to a file and display all scores in a messagebox.
    
    Appends the user's name and score to 'scores.txt' and then reads all
    stored names and scores to display them.
    
    Parameters:
    - name: The user's name as a string.
    - score: The user's score as an integer.
    """
    ### Student Code [8 points -> 4 points per line]:
    # Open the 'scores.txt' file in append mode and write name and score on 
    # separate lines in the file. (Teacher note: file variable name will vary.)
    with open ('scores.txt', 'a') as file:
        file.write(name)
        file.write(score)
    
    scores_text = "Quiz completed!\n\nScores:\n"
    
    ### Student Code [8 points -> 4 points per line]:
    # Open 'scores.txt' again but this time to read the names and scores from
    # the file into a list of strings, saving it in variable scores_list.
    scores_list= []
    with open ('scores.txt', 'r') as file:
        scores_list = file.readline()
        
    
    # Iterate through scores_list, stepping by 2 to get user-score pairs
    for i in range(0, len(scores_list), 2):
        # Prepare the multi-line string of users and scores to be displayed 
        # in the messagebox, in the following format:
        #     username1 : score1
        #     username2 : score2
        #     ...etc.
        scores_text += f"{scores_list[i].strip()}: {scores_list[i+1].strip()}\n"
    
    ### Student Code [4 points]:
    # Display scores_text in an informational messagebox
        messagebox.showinfo('', scores_text)



def next_question():
    """
    Display the next question or show the final scores if the quiz is completed.
    
    Updates the question label to show the next question. If all questions have
    been answered, it saves the current score, displays all scores, and closes
    the application.
    """
    # The following global variables are initialized in the main program, after
    # the function definitions. See their initializations for comments.
    global question_index, num_correct
    
    ### Student Code [24 points -> 4 points per line]:
    # If there are questions left (i.e. the question index is in range of the
    # questions list), process the next question:
    if question_index in range(len(questions)):
        nextquestion = questions[question_index][0]
        question_label.config(text=nextquestion)
    
    
    
    # Else, there are no questions left, so save the user's name and score in
    # the scores file and display the history of saved scores from that file
    # using save_and_display_scores(). Then, close the application:
    else:
        save_and_display_scores(name_entry.get(), num_correct)
        root.destroy()


def check_answer(event=None):
    """
    Check the user's answer against the correct answer and update the quiz
    progress and score.
    
    If the answer is correct, increments the correct answer count.
    Regardless, moves to the next question or ends the quiz if all questions
    have been answered.
    """
    # The following global variables are initialized in the main program, after
    # the function definitions. See their initializations for comments.
    global question_index, num_correct
    
    # If current question index is in range (within the number of questions),
    # check whether the user's answer is correct:
    if question_index < len(questions):   
        # Access and save the answer part of the tuple (the second part):
        correct_ans = questions[question_index][1]
        # Get the user's answer from the entry and strip any extra whitespace:
        user_ans = answerentry.get().strip()
        
        ### Student Code [8 points -> 4 points per line]:
        # If the user's answer is correct (ignoring case), increment the user's 
        # score by 1:
        if user_ans == correct_ans:
            question_index += 1        
            next_question()


"""
Global variables
"""

# questions -> the list with all the questions and answers
# The questions and answers are read from a text file by load_questions().
# Unless another file path is provided to load_questions() as an argument,
# it will read questions and answers from the questions.txt file by default.
questions = load_questions()  

random.shuffle(questions)  # Shuffle questions for a random order each time

# question_index -> The current number of the question in the progression
#     used to access the list item containing the question and track how many
#     questions have been asked.
question_index = 0

# num_correct -> Number of questions user has answered correctly so far.
num_correct = 0


"""
Set up the GUI with widgets for name entry, displaying the current question,
answer entry, and displaying the quiz progress and score.
"""
root = tk.Tk()
root.title("Flashcard Quiz")
root.geometry("500x400")

### Student Code [4 points -> 2 points per line]:
# Create and place a name label called name_label with the text
# "Enter your name:"
name_label = tk.Label(root, text="Enter your name:")
name_label.pack()


### Student Code [4 points -> 2 points per line]:
# Create and place a name entry field called name_entry:
nameentry = tk.Entry(root)
nameentry.pack()


# A label representing a virtual flash card on which to display
# the questions from the file:
question_label = tk.Label(root, text="", height=6, width=60, wraplength=480,
                          borderwidth=2, relief='solid')  
question_label.pack(padx=5, pady=10)

### Student Code [4 points -> 2 points per line]:
# Create and place an answer entry field called answer_entry:
answerentry = tk.Entry(root)
answerentry.pack()

### Student Code [4 points -> 2 points per line]:
# Create and place a button called submit_button with the text "Submit Answer":
submit_button = tk.Button(root, text="Submit Answer:")
submit_button.pack()

### Student Code [4 points]:
# Bind the event where the user presses Enter (event code "<Return>") in the 
# answer entry field. Pressing Enter should submit and check the user's answer:
answerentry.bind("<Return>", check_answer)

### Student Code [4 points -> 2 points per line]:
# Create and place a label called info_label at the bottom of the window.
# Later, this will be configured to display the user's score and how many 
# questions remain, but for now just set the text to be empty ("").
info_label = tk.Label(root, text="")
info_label.pack()
info_label.config(text=f"{num_correct}/{question_index} questions correct; {len(questions)} answers remaining")


"""
Run program
"""
next_question()  # Begin the quiz by showing the first question
root.mainloop()  # Start the GUI event loop