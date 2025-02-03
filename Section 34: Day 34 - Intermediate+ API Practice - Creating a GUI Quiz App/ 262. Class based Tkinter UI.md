Below is one complete implementation of the **ui.py** file for your Quizzler project. This code creates a graphical user interface (GUI) using Tkinter inside a class called `QuizInterface`. It sets up the window, configures the layout, and creates the score label, a canvas for the question text, and the True/False buttons using the images provided in the project folder.

```python
from tkinter import *
# Define a constant for the theme color (midnight blue as provided)
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        # -----------------------
        # Set up the main window:
        # -----------------------
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # -----------------------
        # Score Label (top-right):
        # -----------------------
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12))
        # Place the score label in row 0, column 1
        self.score_label.grid(row=0, column=1)

        # -----------------------
        # Canvas for Question Text:
        # -----------------------
        self.canvas = Canvas(width=300, height=250, bg="white")
        # Create a text item on the canvas at the center.
        self.question_text = self.canvas.create_text(
            150, 125,  # X, Y coordinates (centered: half of width and height)
            width=280,  # Wrap text within 280 pixels
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        # Place the canvas below the score label (row 1) and span two columns.
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # -----------------------
        # True and False Buttons:
        # -----------------------
        # Create the True button using the provided image.
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        
        # Create the False button using the provided image.
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)

        # -----------------------
        # Start the GUI loop:
        # -----------------------
        self.window.mainloop()


# If you want to test the UI independently, you can instantiate QuizInterface:
if __name__ == "__main__":
    QuizInterface()
```

---

### Explanation

- **Window Setup:**  
  - A Tkinter window is created and stored as `self.window`.
  - The window's padding (`padx` and `pady`) is set to 20 pixels, and its background is set to the `THEME_COLOR`.

- **Score Label:**  
  - A label with the text `"Score: 0"` is created. It uses white text on the `THEME_COLOR` background.
  - It is placed in the top-right of the window (row 0, column 1).

- **Canvas & Question Text:**  
  - A canvas of size 300x250 pixels with a white background is created.
  - A text item is added to the canvas at position `(150, 125)` (centered) with a width of 280 pixels, using an Arial 20-point italic font.
  - The canvas is placed in row 1 and spans across two columns, with a vertical padding of 50 pixels to separate it from the score label.

- **Buttons:**  
  - Two buttons are created using the images (`true.png` and `false.png`) found in the `images/` folder.
  - Both buttons have their border (highlightthickness) removed and are placed in row 2; the True button in column 0 and the False button in column 1.

- **Mainloop:**  
  - The GUI event loop is started with `self.window.mainloop()`, ensuring the window stays open and responsive.

You can now run **main.py** (which should import this `QuizInterface` class) to launch your fully laid-out quiz application GUI. Enjoy building your quiz app!
