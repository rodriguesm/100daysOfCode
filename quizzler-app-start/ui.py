import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)

        false_img = tk.PhotoImage(file="images/false.png")
        true_img = tk.PhotoImage(file="images/true.png")

        self.canvas = tk.Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.question_text = self.canvas.create_text(150,125,
                                                     width=280,
                                                     font=("Arial",18,"italic"),
                                                     fill=THEME_COLOR)

        self.score_label = tk.Label(text=f"Score:0",bg=THEME_COLOR,fg="white",font=("Arial",12,"bold"))
        self.score_label.grid(column=1,row=0)

        self.true_button = tk.Button(image=true_img,highlightthickness=0, command=self.click_true)
        self.true_button.grid(column=0,row=2)
        self.false_button = tk.Button(image=false_img,highlightthickness=0, command=self.click_false)
        self.false_button.grid(column=1,row=2)

        self.timer = None
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,text="End of the Quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def click_false(self):
        self.bg_feedback_color(self.quiz.check_answer("false"))


    def click_true(self):
        self.bg_feedback_color(self.quiz.check_answer("true"))


    def bg_feedback_color(self,answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.timer = self.window.after(1000,self.get_next_question)






