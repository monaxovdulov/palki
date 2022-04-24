from tkinter import *
from random import randint
import webbrowser
from tkinter import messagebox

root = Tk()
root.title("Палочки")
root.geometry("300x300")

sticks = 20



def player():
    global sticks
    delete_sticks = int(entry_sticks.get())
    if delete_sticks < sticks and delete_sticks in [1, 2, 3]:
        sticks -= int(delete_sticks)
        lable_sticks.config(text=sticks*"|")
        status.config(text=str(sticks))
    if sticks == 1:
        status.config(text="Вы победили!", fg="green")
        button.config(state=DISABLED)
    else:
        lable_move.config(text="Ход компьютера ожидайте...")
        button.config(state=DISABLED)
        root.after(2000, computer)


def computer():
    global sticks
    delete_sticks = randint(1, 3)
    if delete_sticks < sticks:
        if sticks == 4:
            delete_sticks = 3
        elif sticks == 3:
            delete_sticks = 2
        elif sticks == 2:
            delete_sticks = 1
        sticks -= int(delete_sticks)
        lable_sticks.config(text=sticks*"|")
        status.config(text=str(sticks))
    if sticks == 1:
        status.config(text="Вы проиграли!", fg="red")
        button.config(state=DISABLED)
    else:
        lable_move.config(text="Введите число от 1 до 3")
        button.config(state=NORMAL)
        entry_sticks.focus()


def about():
    """Функция для отображения информации о программе"""
    messagebox.showinfo("О программе",
                        "Больше информации и веселых программ ты найдешь в питонах-батонах.")
    webbrowser.open_new(r"https://t.me/+zjD49vNNAZw5Mzli")


lable_move = Label(text="Введите число от 1 до 3", font=("Arial", 12, "bold"), padx=10, pady=10)
lable_move.pack()

entry_sticks = Entry(font=("Arial", 12, "bold"))
entry_sticks.pack()

lable_sticks = Label(text="|" * sticks, font=("Arial", 30, "bold"), padx=10, pady=10, )
lable_sticks.pack()

status = Label(text=sticks, font=("Arial", 30, "bold"))
status.pack()

button = Button(text="Взять палочки", font=("Arial", 15, "bold"), command=player)
button.pack()

mainmenu = Menu(root)
root.config(menu=mainmenu)
mainmenu.add_command(label='О программе', command=about, accelerator="Ctrl+A", underline=0)


root.mainloop()
