from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        print(self.quiz)
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text="Some text",
                                                font=FONT,
                                                fill="black")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true = Button(image=self.true_img,
                           highlightthickness=0,
                           highlightbackground=THEME_COLOR,
                           command=self.answer_true)
        self.true.grid(row=2, column=0)
        self.false = Button(image=self.false_img,
                            highlightthickness=0,
                            highlightbackground=THEME_COLOR,
                            command=self.answer_false)
        self.false.grid(row=2, column=1)

        self.timer = self.window.after(100, self.get_next_question)
        self.window.mainloop()

    def get_next_question(self):
        self.window.after_cancel(self.timer)
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"Your score is {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.timer = self.window.after(1000, self.get_next_question)