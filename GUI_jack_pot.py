import tkinter as tk
import random


root = tk.Tk()
root.title("Welcome to Jack Pot world")
root.geometry("350x280")


complete = ['watermelon', 'watermelon', 'watermelon', 'cherry', 'cherry', 'cherry',
           'grapes', 'grapes', 'grapes', 'plum', 'plum', 'plum', 'diamond', 'diamond',
           'diamond', 'lemon', 'lemon', 'lemon', '7', '7', '7']

without = ['watermelon', 'watermelon', 'watermelon', 'cherry', 'cherry', 'cherry',
            'grapes', 'grapes', 'grapes', 'plum', 'plum', 'plum', 'diamond', 'diamond',
            'diamond', 'lemon', 'lemon', 'lemon', '7', '7']

attempt = 10

def start_game():
    global attempt
    if attempt < 100:
        result = random.choices(without, k=3)
        #result = random.choices(complete, weights= [25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25, 25, 25, 1], k=3)
        if result == ['7', '7', '7']:
            label_result.config(text = '7 7 7\nCongratulations! You are a Millionaire!', fg='red', font=("Helvetica", 13, 'bold'))
            start_button.config(state=tk.DISABLED)
        else:
            label_result.config(text = '{} {} {}'.format(result[0], result[1], result[2]), fg='red')
        attempt += 10
    else:
        #result = random.choices(complete, k=3)
        result = random.choices(complete, weights= [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1, 25, 25, 25], k=3)
        if result == ['7', '7', '7']:
            label_result.config(text = '7 7 7\nCongratulations! You are a Millionaire!', fg='red', font=("Helvetica", 13, 'bold'))
            start_button.config(state=tk.DISABLED)
        else:
            label_result.config(text = '{} {} {}'.format(result[0], result[1], result[2]), fg='red')
        attempt += 10
        

def exit_function():
    root.destroy()


welcome_label = tk.Label(root, text="Welcome to our Jack Pot application", font=("Helvetica", 12))
welcome_label.pack(pady=(10, 5))

prize_text = tk.Text(root, height=1, borderwidth=0, font=("Helvetica", 10))
prize_text.tag_configure("bold_red", font=("Helvetica", 10, "bold"), foreground="red")
prize_text.insert("1.0", "Jack Pot is an incredible ")
prize_text.insert(tk.END, "1 million $", "bold_red")
prize_text.configure(state="disabled", relief="flat")
prize_text.pack(padx=67, pady=(0, 10))

start_game_label = tk.Label(root, text="When you are ready please press button 'Start'", font=("Helvetica", 10))
start_game_label.pack()

start_button = tk.Button(root, text='Start', command=start_game)
start_button.pack(pady=10)

label_result = tk.Label(root, text='')
label_result.pack()                       

continue_label = tk.Label(root, text="If you like to quit game please press button 'Exit'", font=("Helvetica", 10))
continue_label.pack(pady=10)

exit_button = tk.Button(root, text='Exit', command=exit_function)
exit_button.pack()

root.mainloop()
