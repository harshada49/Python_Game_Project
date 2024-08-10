import math
import random
import tkinter as tk


root = tk.Tk()
root.geometry("700x600")
root.title("Square and Square Roots Game")

def start_game():
    player_name=name_entry.get()
    question_label.config(text=f"Ready,{player_name}? your question will appear here.",bg="alice blue",font=("Bell MT",16))
    answer_entry.config(state=tk.NORMAL)
    submit_button.config(state=tk.NORMAL)


def check_answer():
    question_label2.config(text=f"Checking answer : {answer_entry.get()}")

def quit_game():
    root.quit()

tk.Label(root, text="Welcome to the Game!",bg="alice blue",font=("Chiller",50,"bold")).pack(pady=20)
tk.Label(root, text="Please Enter Your Name:",fg="red",bg="alice blue",font=("Bell MT",22)).pack(pady=15)
name_entry=tk.Entry(root,width=30)
name_entry.pack(pady=6,ipady=5)

button=tk.Button(root,text="start game", command=start_game, fg="dark green",font=("Bell MT",15))
button.pack(pady=10)

question_label=tk.Label(root,text=" ",font=("Bell MT",18),bg="alice blue")
question_label.pack(pady=15)

tk.Label(root,text="your answer:",font=("Bell MT",15),bg="alice blue").pack(pady=10)
answer_entry=tk.Entry(root,state=tk.DISABLED)
answer_entry.pack(pady=5,ipady=2)

submit_button = tk.Button(root,text="Submit answer",command=check_answer, fg="dark green")
submit_button.pack(pady=5,ipady=2)

question_label2=tk.Label(root,text=" ",font=("Bell MT",14),bg="alice blue")
question_label2.pack(pady=15)

quit_button = tk.Button(root,text="Quit Game", command = quit_game)
quit_button.pack(pady=5)

root.configure(bg="alice blue")
root.mainloop()
