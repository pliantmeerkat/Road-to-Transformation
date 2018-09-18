from random import *

RULES =("Rules:\n"
        "the piece will last the time taken to play all chords in order and\n"
        "then in retrograde\n"
        "instrumentation/ time signiture/ rhythm can be chosen by performers\n"
        "only notes from the chords may be used\n"
        "the piece will uses divisions of 3 with the 1st line playing all\n"
        "notes in the triad, the 2nd notes playing 2 of their choice-\n"
        "and the 3rd playing 1, all lines work in cannon,\n"
        "with 1 leading and 2 following after 1 chord etc..\n"
        "use as mnany or little chords as you wish\n"
        "all chords generated follow Neo-Riemannian Theory\n"
        "R stands for root chord\n")



##GENERATOR CODE
class generate():
  def __init__(self):
      self = str

  def key_select(self):
      k_choice = randint(1,12)
      if k_choice == 1:
          k = "C"
      elif k_choice == 2:
          k = "C#"
      elif k_choice == 3:
          k = "D"
      elif k_choice == 4:
          k = "D#"
      elif k_choice == 5:
          k = "E"
      elif k_choice == 6:
          k = "F"
      elif k_choice == 7:
          k = "F#"
      elif k_choice == 8:
          k = "G"
      elif k_choice == 9:
          k = "G#"
      elif k_choice == 10:
          k = "A"
      elif k_choice == 11:
          k = "A#"
      elif k_choice == 12:
          k = "B"
      t_choice = randint(1, 2)
      if t_choice == 1:
          t = "Major"
      elif t_choice == 2:
          t = "Minor"
      return k, t

  def chord_picker(self):
    chord = randint(1, 21)
    if chord == 1 or chord == 2 or chord == 3 or chord == 4:
      C = "L"
    elif chord == 5 or chord == 6 or chord == 7 or chord == 8:
      C = "P"
    elif chord == 9 or chord == 10 or chord == 11 or chord == 12:
      C = "R"
    elif chord == 13 or chord == 14:
      C = "H"
    elif chord == 15 or chord == 16:
      C = "N"
    elif chord == 17 or chord == 18:
      C = "S"
    elif chord == 19 or chord == 20 or chord == 21:
      C = "A"
    return C
    
    


##TRANSLATOR CODE
class translate():
  def __init__(self):
    self = str

  def num_assign(self, key):
    ##C = 10, D = 20, E = 30, F = 35, G = 45, A = 55, B = 65
    if key == "C":
      num = 10
    elif key == "C#":
      num = 15
    elif key == "D":
      num = 20
    elif key == "D#":
      num = 25
    elif key == "E":
      num = 30
    elif key == "F":
      num = 35
    elif key == "F#":
      num = 40
    elif key == "G":
      num = 45
    elif key == "G#":
      num = 50
    elif key == "A":
      num = 55
    elif key == "A#":
      num = 60
    elif key == "B":
      num = 65
    return num
 
  def key_code(self, num):
    if num > 65:
      num -= 60
    if num < 10:
      num += 60
   
    if num == 10:
      key = "C"
    elif num == 15:
      key = "C#"
    elif num == 20:
      key = "D"
    elif num == 25:
      key = "D#"
    elif num == 30:
      key = "E"
    elif num == 35:
      key = "F"
    elif num == 40:
      key = "F#"
    elif num == 45:
      key = "G"
    elif num == 50:
      key = "G#"
    elif num == 55:
      key = "A"
    elif num == 60:
      key = "A#"
    elif num == 65:
      key = "B"
    return key
   
  def tonality(self, ton):
    if ton == "Major":
      ton = "Minor"
    elif ton == "Minor":
      ton = "Major"
    return ton
   
  def L_tran(self, t, pi):
    N = I.num_assign(pi)
    if t == "Major":
      N += 20
    elif t == "Minor":
      N -= 20
    P = t
    p = I.tonality(P)
    KY = I.key_code(N)
    return p, KY
 
  def P_tran(self, t, pi):
    N = I.num_assign(pi)
    P = t
    p = I.tonality(P)
    KY = I.key_code(N)
    return p, KY
 
  def R_tran(self, t, pi):
    N = I.num_assign(pi)
    if t == "Major":
      N += 45
    elif t == "Minor":
      N -= 45
    P = t
    p = I.tonality(P)
    KY = I.key_code(N)
    return p, KY
 
  def l_tran(self, t, pi):
    N = I.num_assign(pi)
   
   
    P = T
    KY = I.key_code(N)
    return p, KY
   
  def H_tran(self, t, pi):
    N = I.num_assign(pi)
    if t == "Major":
      N -= 20
    elif t == "Minor":
      N += 20
    P = t
    p = I.tonality(P)
    KY = I.key_code(N)
    return p, KY
 
  def N_tran(self, t, pi):
    N = I.num_assign(pi)
    if t == "Major":
      N += 25
    elif t == "Minor":
      N -= 25
    P = t
    p = I.tonality(P)
    KY = I.key_code(N)
    return p, KY
   
  def S_tran(self, t, pi):
    N = I.num_assign(pi)
    if t == "Major":
      N += 5
    elif t == "Minor": 
      N -= 5
    P = t
    p = I.tonality(P)
    KY = I.key_code(N)
    return p, KY

  ### augmented chords code(U = UP, D = DOWN
 ##LPR refers to usage for major chords
  #C = 10, D = 20, E = 30, F = 35, G = 45, A = 55, B = 65
  def Aug(self, t, pi):
    T = t
    T = "Aug"
    #print(pi, T)
    T, pi = I.Aug_pick(t, pi)
    return T, pi

  def Aug_pick(self, t, pi):
    T = t
    P = pi
    A = randint(1, 6)
    if A == 1:
      T, P = I.U_aug_L(t, pi)
    if A == 2:
      T, P = I.U_aug_P(t, pi)  
    if A == 3:
      T, P = I.U_aug_R(t, pi)
    if A == 4:
      T, P = I.D_aug_L(t, pi)
    if A == 5:
      T, P = I.D_aug_P(t, pi)
    if A == 6:
      T, P = I.D_aug_R(t, pi)
    return T, P

  def U_aug_L(self, t, pi):
    t = "Minor"
    N = I.num_assign(pi)
    N += 5
    KY = I.key_code(N)
    return t, KY
    
  def U_aug_P(self, t, pi):
    t = "Minor"
    N = I.num_assign(pi)
    N += 25
    KY = I.key_code(N)
    return t, KY

  def U_aug_R(self, t, pi):
    t = "Minor"
    N = I.num_assign(pi)
    N += 45
    KY = I.key_code(N)
    return t, KY

  def D_aug_L(self, t, pi):
    t = "Major"
    N = I.num_assign(pi)
    N += 20
    KY = I.key_code(N)
    return t, KY

  def D_aug_P(self, t, pi):
    t = "Major"
    N = I.num_assign(pi)
    N += 40
    KY = I.key_code(N)
    return t, KY
    
  def D_aug_R(self, t, pi):
    t = "Major"
    KY = pi
    return t, KY


I = translate()
