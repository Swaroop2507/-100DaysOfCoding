
def get_next_question(self):
    # Reset the canvas background no matter what
    self.canvas.config(bg="white")
    
    # Check if there are still questions available
    if self.quiz.still_has_questions():
        # Update the score label
        self.score_label.config(text=f"Score: {self.quiz.score}")
        
        # Get the next question text and update the canvas text item
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
    else:
        # If no questions are left, let the user know and disable the answer buttons
        self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

def give_feedback(self, is_right):
    """
    Change the canvas color to green if the user answered correctly,
    or red if they answered incorrectly. After one second, move on
    to the next question.
    """
    if is_right:
        self.canvas.config(bg="green")
    else:
        self.canvas.config(bg="red")
    
    # Wait for 1000ms (1 second) then call get_next_question (without parentheses)
    self.window.after(1000, self.get_next_question)

def true_pressed(self):
    """
    Called when the 'True' button is pressed. Checks the answer,
    then provides visual feedback.
    """
    is_right = self.quiz.check_answer("True")
    self.give_feedback(is_right)

def false_pressed(self):
    """
    Called when the 'False' button is pressed. Checks the answer,
    then provides visual feedback.
    """
    is_right = self.quiz.check_answer("False")
    self.give_feedback(is_right)
Explanation
get_next_question Method:

Resets the canvas background to white.
Checks if there are still questions left using self.quiz.still_has_questions().
If yes, it fetches the next question (and updates the score label) and displays the question on the canvas.
If not, it updates the canvas to inform the user that the quiz has ended and disables the True/False buttons.
give_feedback Method:

Changes the canvas background to green if the answer was correct or red if it was wrong.
Uses self.window.after(1000, self.get_next_question) to wait 1 second before moving to the next question. Notice that the function reference self.get_next_question is passed without parentheses.
Button Press Methods (true_pressed and false_pressed):

These methods call the quiz brain’s check_answer method, which returns a Boolean.
Then they call give_feedback with that Boolean to display the appropriate color and transition to the next question.
This snippet reflects the exact functionality described in the transcript. You can adapt it into your full quiz application accordingly.







