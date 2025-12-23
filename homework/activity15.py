import tkinter as tk
import random
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("350x300")
choices = ["Rock", "Paper", "Scissors"]
def play(user_choice):
    computer_choice = random.choice(choices)
    user_label.config(text="Your Choice: " + user_choice)
    comp_label.config(text="Computer Choice: " + computer_choice)
    if user_choice == computer_choice:
        result_label.config(text="Result: It's a Tie!", fg="blue")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result_label.config(text="Result: You Win! ", fg="green")
    else:
        result_label.config(text="Result: You Lose ", fg="red")
tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold")).pack(pady=10)
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_label.pack()
comp_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
comp_label.pack()
result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=10)
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

root.mainloop()
