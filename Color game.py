import tkinter
import random

colors=["Red","Blue","Green","Pink","Black","Yellow","Orange","White","Purple",
"Black"]

timeleft=30
point = 0

#function that will start the game
def startGame (event):
    if timeleft==30:
        print("Hello")
        countdown()
    nextColor()
    
def countdown(): # starting the timer
    global timeleft
    if timeleft>0:
        timeleft=timeleft-1 #decrement the timer
        timeText.config(text="Time Left:"+str(timeleft))
        timeText.after(1000, countdown)

def nextColor():
    global point
    global timeleft
    if timeleft > 0: #a game is currently in play
        answer.focus_set()
        if answer.get().lower()==colors[1].lower():
            point=point+1
        answer.delete(0, tkinter.END) # clear the whitebox
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0])) #show the color of 

        score.config(text="score:" +str(point)) #Update the point

window=tkinter.Tk()

window.title("Color Typing Game")

window.geometry("400x200")

instructions=tkinter.Label(window, text="Type in color of the words")
instructions.pack()

score=tkinter.Label(window, text="Press enter to start")
score.pack()

timeText=tkinter.Label(window, text="Time left:" + str(timeleft))
timeText.pack()

label=tkinter.Label(text="",font=('Helvertica',60))
label.pack()

answer=tkinter.Entry(window) #This is for making a whitebox
# We are going to start the game when user pressenter
window.bind('<Return>', startGame)
answer.pack()
answer.focus_set()

window.mainloop()


