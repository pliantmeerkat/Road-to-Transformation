import tkinter
from tkinter import *
import random
import linecache
from Source.prog import *
import Source.Buttons
from Source.Buttons import *
from Audio.Audio import *

## Rules:
#the piece will last the time taken to play all chords in order and then in retrograde
#instrumentation/ time signiture/ rhythm can be chosen by performers
#only notes from the chords may be used
#the piece will uses divisions of 3: with the 1st line playing-
#all notes in the triad, the 2nd notes playing 2 of their choice-
#and the 3rd playing 1,all lines work in cannon, with 1 leading and 2 following after 1 chord etc..
#use as mnany or little chords as you wish
#all chords generated follow Neo-Riemannian Theory
# R stands for root chord

C = str
T = str
K = str
running = bool
G = generate()
I = translate()

###GUI CODE
class UI():
  def __init__(self):
    self = scrn

  def boot(self):
    scrn.geometry("600x400+300+300")
    scrn.configure(background="red")
    scrn.title("road to transformation v1.11")
    ##icon to be created..
    #scrn.wm_iconbitmap("..")
    
    ##configuring and packing buttons from buttons.py
   
    B_frame.pack(side= BOTTOM)

    T_frame.pack(side= TOP)

    mb.pack()
     
    L_B.configure(command = lambda: U.Start_Scrn())

    L_B.pack()
    
    

  def Start_Scrn(self):
    ##code for loading the menu screen upon running the program
      L_B.pack_forget()
      
      O_1.configure(command = lambda: U.pre_init())
      O_2.configure(command = lambda: U.manual())
                                               
                           
      O_1.pack(side=tkinter.LEFT)
      O_2.pack(side=tkinter.RIGHT)
      A.Start_Sound()


  def manual(self):
    #WIP will eventually be for inputing NRT strings to create
    #custom chord sequences!
    
    
    
    
    Man_B.configure(command = lambda: U.Man_func())
    Back_B.configure(command = lambda: U.E_Return())

    O_1.pack_forget()
    O_2.pack_forget()
    Man_B.pack(side=tkinter.LEFT)
    Back_B.pack(side=tkinter.RIGHT)
    Man_T.pack()
    L_info.pack()
    
                           
  def Man_func(self):
    #function dealing with mnual button iput
    Key = Man_T.get()
    File = open("configuration file.ini", "w")
    File.write(Key)
    L_info.configure(text = "Now type in your transformations\n in CAPITALS,"
                     "\nusing the letters L,P,R,H,S,N,A")
    L_info.pack()
    G = Man_T.get()
    Read = open("configuration file.ini", "r")
    KAns = Read.read()
    print("R = ", KAns)
    print(G)
  
  def E_Return(self):
    #main return function, closing all nescesary buttons
    Man_B.pack_forget()
    Back_B.pack_forget()
    mb.pack_forget()
    Txt.pack_forget()
    B_frame.pack_forget()
    T_frame.pack_forget()
    L_info.pack_forget()
    Man_T.pack_forget()
    U.boot()
    

  def pre_init(self):
    O_1.pack_forget()
    O_2.pack_forget()
    U.initialise()

  def initialise(self):
    
    scrn.configure(background="green")
    T_B.configure(command = lambda: U.Run())
    R_B.configure(command = lambda: U.Repeat_func())
    
    
    Ret.configure(command = lambda : U.Ret2())
    B_2.configure(command = lambda: U.rules())
    B_Q.configure(command = lambda:U.QUIT())
    B_1.configure(command= lambda: U.B_start())                   
    
    Y_B.configure(command = lambda: U.Quit_Total(scrn))
    N_B.configure(command = lambda: U.Return())

   


    
    B_1.pack(side = tkinter.LEFT)
    B_2.pack(side = tkinter.LEFT)
    B_Q.pack(side= tkinter.RIGHT)
    #L_1.pack()
    L_2.pack()

  def func():
    intro = "your start key is"
    
    pass
    L2.configure(text= "",
                 fg = "black",
                 bg = "orange",
                 width= 55,
                 height = 15,
                 font="helvetica 12 ")
  
  def Repeat_func(self):
    ##may be cut from final version.
    X = linecache.getline("road to transformation.txt", 19)
    KTON = linecache.getline("configuration file.ini", 2)
    i = 0
    ton = ""
    for w in KTON:
      if i == 0:
        k = w
      
      elif i >= 2:
        ton = (w + ton)
      
        P = ton[::-1]

      i += 1
    X += X
     
    trans_loop(k, P, X)
    return "  N"
    

  def Run(self):
      ##excecutes the main algorithm upon activation
      LA2 = L_2
      T_B.pack_forget()
      Num = Txt.get()
      Txt.pack_forget()
      
      try:
        k, ton, G = generator_loop(Num)
        K = k
        T = ton
        Chords = trans_loop(k, ton, G)
        F = open("configuration file.ini", "w")
        F.write("Here is your generated Start Key:\n" )              
        F.write(K)
        F.write(" ")
        F.write(T)
        F.write("\nYou can find the complete chord sequence\n"
                      "in the attached file!")

        F = open("configuration file.ini", "r")
        Li_1 =F.readline()
        Li_2 = F.readline()
        Li_3 = F.readline()
        Li_4 = F.readline()
        Li_T = (Li_1 + Li_2 + Li_3 + Li_4)
        L_1.configure(text="Results:")
                      


        L_2.configure(text=Li_T,
                      font=("helvetica 19 bold"))

        
        C_B.configure(command = lambda: U.Play_Score(K, T, Chords))
        
                      
        C_B.pack(side = tkinter.RIGHT)
        R_B.pack(side=tkinter.LEFT)

        Ret.pack(side=tkinter.RIGHT)
        L_2.pack()

          ##potential output code
          #output_file = os.path.join(main_dir, "road to transformation.txt")
          #output = "notepad.exe road to transformation.txt"
          
          #os.system(output)
      except:
        LA2.configure(text="error, press back to return\n"
                      "or quit and restart :(\n\n"
                      "Remeber to enter only numbers!",
                      fg = "blue",
                      bg = "red",
                      font="helvstica 22 bold")
        LA2.pack()
        Ret.pack(side=tkinter.RIGHT)

     
      
    
    
    

  def B_start(self):
    B_1.pack_forget()
    B_2.pack_forget()
    L_1.configure(text = "Enter your number Of chords please")
    L_2.pack_forget()

    
    Txt.pack()
    T_B.pack()
    
    
    
    

  def rules(self):
    L_2.configure(text=RULES,
                    font="helvetica 14")
    
  def Play_Score(self, K, T, Chords):
    Start = (K + " " + T)
    A.Play_func(Start)
    A.Play_func(Chords)
    

  def QUIT(self):
    Ret.pack_forget()
    C_B.pack_forget()
    L_1.pack_forget()
    B_1.pack_forget()
    B_2.pack_forget()
    B_Q.pack_forget()
    R_B.pack_forget()
    T_B.pack_forget()
    Txt.pack_forget()
    L_2.configure(text="Are you sure you want to Quit?",
                  bg = "green",
                  font=("helvetica 28 bold"))
                        
    
    
    
    L_2.pack()
    Y_B.pack(side=tkinter.LEFT)
    N_B.pack(side=tkinter.RIGHT)
    T_frame.forget()
    scrn.configure(background="green")

  def Ret2(self):
    C_B.pack_forget()
    Ret.pack_forget()
    L_2.pack_forget()
    B_Q.pack_forget()
    R_B.pack_forget()

    U.initialise()
  
  def Return(self):
    C_B.pack_forget()
    L_2.pack_forget()
    Y_B.pack_forget()
    N_B.pack_forget()
    

    U.initialise()


  def Quit_Total(self, root):
    F = open("configuration file.ini", "w")
    F.write("")
    root.destroy()
    A.End_Sound()
    quit()    
    
    
   
#class Assignment
U = UI()
A = Sound_Class()
def UI_loop():
  #parent function for UI 
  U.boot()
  scrn.mainloop()
  A.End_Sound()

def generator_loop(Num):
  ##loop for creating the NRT transformations
  O = ""
  k, ton = G.key_select()
  C = k, ton
  ##int(input("type in the number of chords"))
  I = int(Num)
  for i in range(I):
    B = G.chord_picker()
    O = (O + B)

  return k, ton, O

def write_output(chords, output, key, tone, file):
  ##code to write the output of the programs using a set template
  F = open(file, "w")
  F.write(RULES)
  F.write("\n\n\n\nYour Transformations are written below\n\n")
  F.write(chords)
  F.write("\n\n")
  F.write("Your start key is ")
  F.write(key)
  F.write(" ")
  F.write(tone)
  F.write("\n\nAnd here are your chords, not incluiding start!\n\n")
  F.write(output)
  F.write("\n\nThanks for using this in devellopment program!\n\nRemember that"
          "whilst you must follow the rules stringlenty there is much room for creativity and self expression!\n"
          "so let the creative juices flow and produce some great music!!!")
  F.write("\n\n\nthis file will be overwritten upon program use so "
          "please save a copy of this file elsewhere \n"
          "if you wish to keep the chord sequence generated")
  F.write("\n\n\n\n\nProgram coded and created by Jack Branch, ask permission before distributing.")




def main_menu(init):

  choice = "N"

  return choice
  

def trans_loop(kk, to, imp):
  ##translator loop of the NRT output generator
  KEY = kk
  TONE = to
  PI = ""
  J = ""
  a = "Aug"
  init = 0
  ton = to
  k = kk
  TO = k
  
  running = True
  X = imp
  while running == True:
    init = 1
    #try:
    for i in range(0, len(X)):
      C = X[i]
     
      if C == "L":
        TO, PI = I.L_tran(ton, k)
      elif C == "P":
        TO, PI = I.P_tran(ton, k)
      elif C == "R":
        TO, PI = I.R_tran(ton, k)
      elif C == "H":
        TO, PI = I.H_tran(ton, k)
      elif C == "N":
        TO, PI = I.N_tran(ton, k)
      elif C == "S":
        TO, PI = I.S_tran(ton, k)
      elif C == "A":
        J = (J+ (PI +" "+a) +"\n")
        TO, PI = I.Aug(ton, k)
        #J = (J+(PI+ " "+TO) + "\n")
      
        
        
      J = (J+(PI+" "+TO) + "\n")
      ton = TO
      k = PI
 
      

    
    end = main_menu(init)
    write_output(X, J, KEY, TONE, "road to transformation.txt")
    return J
    if end == "N":
      break

    
    
  

def main_loop():
  ##main program function
  UI_loop()
  k, ton, G = generator_loop()
  trans_loop(k, ton, G)
  
     
main_loop()


     

