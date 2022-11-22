from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
import time
import random
gcash = 200
def color():
    colors = colorchooser.askcolor()
    colorshex = colors[1]
    print(colorshex)
    random_window.config(bg=colorshex)


def insert_cash():
    global gcash
    gcash = 200
    label2.config(text="Your balance is:" + str(gcash))

def playbet():
    global gcash
    bet = int(your_bet.get())
    return bet



def guess():
    player_guess = int(player_entry.get())
    return player_guess


def gamble(c):
    cash = c
    bet = playbet()
    Guess = guess()
    if bet <= cash:
        C = ["J", "Q", "K", "A"]
        random.shuffle(C)
        if 0 < Guess < 5:
            if Guess - 1 == C.index("Q"):
                cash += 3 * bet
                messagebox.showinfo(title="YOU WON! THE POSITIONS ARE:",
                                    message=C)

            else:
                cash -= bet
                messagebox.showinfo(title="YOU LOST! THE POSITIONS ARE:",
                                    message=C)


        else:
            messagebox.showerror(title="INVALID ATTEMPT",
                                 message="TRY ANOTHER POSITION PLEASE")
    else:
        messagebox.showerror(title="INVALID ATTEMPT",
                                 message="INSERT MORE CREDITS PLEASE")

    return cash
def calc():
    global gcash
    helping = gamble(gcash)
    gcash = helping
    label2.config(text="Your balance is:" + str(gcash))

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

# -----------------------------------------------------

random_window = Tk()
random_window.geometry("1080x600")
random_window.title("CARDS GAMBLING")
random_window.config(bg="#004000")
label = Label(random_window, text="***Welcome to Casino RITZ***", bg="#cc0000",
              fg="gold",
              font=("Times", 44, "bold")
              )
label.pack()
label2 = Label(random_window, text="Your balance is:"+str(gcash),
               bg="#004000", fg="grey", font=("Arial", 20, "bold"))
label2.place(x=400, y = 320)
label3 = Label(random_window, text="PLACE YOUR BET HERE PLEASE:",
               bg="gold", fg="#004000", font=("Arial", 14, "bold"))
label3.place(x=15, y=300)
label4 = Label(random_window, text="CHOOSE A POSITION FROM 1 TO 4:",
               bg="gold", fg="#004000", font=("Arial", 14, "bold"))
label4.place(x=730, y=300)
main_label = Label(random_window,
                   text="?CAN YOU GUESS THE POSITION OF THE QUEEN?",
                   bg="gold", fg="#004000", font=("Verdana", 28, "bold"))
main_label.place(x=25, y=200)
button1 = Button(random_window, text="Insert cash",
                 bg="green",
                 fg="black",
                 font=("Arial", 10, "bold"),
                 activebackground="green",
                 activeforeground="red",
                 command=insert_cash)
button1.place(x=80, y=100)

button_color = Button(random_window,
                      text="Background Color",
                      command=color,
                      font=("Arial", 9, "bold"))
button_color.place(x=880, y=100)

your_bet = Entry(random_window, font=("Arial", 20))
your_bet.place(x=20, y=330)
player_entry = Entry(random_window, font=("Arial", 20))
player_entry.place(x=750, y=330)

button_submitbet = Button(random_window, text="      BET        ",
                          font=("Arial", 10, "bold"),
                          command=playbet).place(x=120,y=380)

button_submitGuess = Button(random_window, text="PLAY THIS POSITION",
                            font=("Arial", 10, "bold"),
                            command=guess).place(x=830,y=380)

button_play = Button(random_window, text="       PLAY        ",
                     font=("Arial", 15, "bold"),
                     command=calc).place(x=450, y=380)
# -------------------------------- MOVING WIDGETS
#.bind("<Button-1>", drag_start)
#.bind("<B1-Motion>", drag_motion)
#.bind("<Button-1>", drag_start)
#.bind("<B1-Motion>", drag_motion)
# --------------------------------ANIMATIONS
xVelocity = 5
HEIGHT = 180
WIDTH = 600
canvas = Canvas(random_window, width=WIDTH, height=HEIGHT)
canvas.place(x=230, y=440)
bg = PhotoImage(file="BG.png")
bg_image = canvas.create_image(300, 90, image=bg)
queen = PhotoImage(file="QUEEN.png")
queen_image = canvas.create_image(60,90 ,image=queen)
while True:
    random_window.update()
    coordinates = canvas.coords(queen_image)
    time.sleep(0.0001)
    if(coordinates[0] >= WIDTH or coordinates[0] < 0):
        xVelocity = -xVelocity
    canvas.move(queen_image, xVelocity, 0)

random_window.mainloop()
