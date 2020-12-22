from tkinter import *
import time

def times():
    #the current time is in the object of current_time
    current_time = time.strftime("%I:%M:%S:%p")   #The strftime() function is used to convert date and time objects to their string representation.

    a=Label(root, font="berlin 80", bg="black", fg="red", text=current_time)
    a.after(200,times)
    a.grid(row=0,column=1)

root=Tk()
root.title("Digital clock")
root.resizable(False,False)
times()
root.mainloop()