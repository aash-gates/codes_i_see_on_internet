import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

playera = tk.StringVar()
playerb = tk.StringVar()
p1 = tk.StringVar()
p2 = tk.StringVar()


player1_name = tk.Entry(root, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = tk.Entry(root, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)


bclick = True
flag = 0

buttons = tk.StringVar()


def disableButton():
    button1.configure(state="disabled")
    button2.configure(state="disabled")
    button3.configure(state="disabled")
    button4.configure(state="disabled")
    button5.configure(state="disabled")
    button6.configure(state="disabled")
    button7.configure(state="disabled")
    button8.configure(state="disabled")
    button9.configure(state="disabled")


def btnclick(buttons):
    global bclick, flag, player1_name, player2_name, playerb, playera

    if buttons["text"] == " " and bclick==True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        playera = p1.get() + " Wins!"
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
