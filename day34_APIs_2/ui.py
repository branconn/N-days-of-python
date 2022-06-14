THEME_COLOR = "#375362"
import tkinter as tk
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, qb: QuizBrain):  # major key, bro
        self.qb = qb
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.canvas = tk.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.label_s = tk.Label(text=f"Score: {self.qb.score} / {self.qb.question_number}", bg=THEME_COLOR, fg="white")
        self.label_s.grid(row=0, column=1)

        right_img = tk.PhotoImage(file="images/true.png")
        self.right = tk.Button(image=right_img, highlightthickness=0, command=self.right)
        self.right.grid(row=2, column=0)

        wrong_img = tk.PhotoImage(file="images/false.png")
        self.wrong = tk.Button(image=wrong_img, highlightthickness=0, command=self.wrong)
        self.wrong.grid(row=2, column=1)

        self.get_new_q()

        self.window.mainloop()

    def get_new_q(self):
        self.canvas.config(bg="white")
        q_text = self.qb.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def right(self):
        self.final_answer("True")

    def wrong(self):
        self.final_answer("False")

    def final_answer(self, answer):
        if self.qb.check_answer(answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.label_s.config(text=f"Score: {self.qb.score} / {self.qb.question_number}")
        if self.qb.question_number > 9:
            self.end_game()
        else:
            self.window.after(500, self.get_new_q)

    def end_game(self):
        self.canvas.itemconfig(self.question_text,
                               text=f"You answered {self.qb.score} out of {self.qb.question_number} correct")

