import tkinter
from tkinter import *
##screen variables

scrn = tkinter.Tk()
B_frame= Frame(scrn)
T_frame = Frame(scrn)
##labels
L_info = tkinter.Label(scrn, text="Type in your start key please\n"
                           "You Must format like this:\n 'C Major'",
                           fg = "black",
                           bg = "white",
                           width = 35,
                           height = 30,
                           font="helvetica 25 bold")
L_1 = tkinter.Label(T_frame,
                        fg = "red",
                        bg = "green",
                        font="helvetica 25 bold")

L_2 = tkinter.Label(scrn, text="Welcome!",
                        fg = "Black",
                        bg = "white",
                        width= 55,
                        height = 15,
                        font="helvetica 24 ")

##text boxes
Txt = Entry(scrn, bd=5)
Man_T = Entry(scrn, bd=5)

##button list

mb = Menubutton(scrn, text="Options", relief=RAISED, width=7)
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu




#butons in chronological order:

L_B = tkinter.Button(B_frame, text="Begin",
                         fg = "yellow",
                         bg = "black",
                         font = "helvetica 30 bold")
O_1 = tkinter.Button(B_frame, text="Generate",
                           fg = "green",
                           bg = "violet",
                           font=("helvetica 25 bold"))
                          
O_2 = tkinter.Button(B_frame, text="Manual",
                           fg = "blue",
                           bg = "orange",
                           font=("helvetica 25 bold"))

Man_B = tkinter.Button(B_frame, text= "Enter",
                           fg = "blue",
                           bg = "yellow",
                           font="helvetica 25 bold")                       

Back_B = tkinter.Button(B_frame, text="Back",
                            fg = "yellow",
                            bg = "blue",
                            font="helvetica 25 bold")
T_B = tkinter.Button(scrn, text="Continue",
                         fg = "blue",
                         bg = "green",
                         font= "helvetics 22 bold")
R_B = tkinter.Button(B_frame, text="Repeat",
                         fg = "blue",
                         bg = "green",
                         font="helvetica 30 bold")
Ret = tkinter.Button(B_frame,
                           text = "Back",
                           fg = "blue",
                           bg = "red",
                           font="helvetics 30 bold")
B_2 = tkinter.Button(B_frame, text="Info",
                         fg = "blue",
                         bg = "yellow",
                         font="helvetica 30 bold")
B_Q = tkinter.Button(B_frame, text="Quit",
                         fg = "red",
                         bg = "violet",
                         font="helvetics 30 bold")
B_1 = tkinter.Button(B_frame, text="start",
                         fg = "yellow",
                         bg = "blue",
                         font="helvetica 30 bold")
C_B = tkinter.Button(B_frame, text="Play",
                         fg = "blue",
                         bg = "green",
                         font="helvetica 30 bold")
Y_B = tkinter.Button(B_frame, text="Yes",
                         fg = "blue",
                         bg = "green",
                         font="helvetica 22 bold")
N_B = tkinter.Button(B_frame, text= "No",
                         fg = "red",
                         bg = "green",
                         font="helvetica 22 bold")

