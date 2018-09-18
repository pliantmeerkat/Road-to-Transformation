import winsound
from winsound import *
import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

##chord audio files
CMaj = os.path.join(main_dir, "CMaj.wav")
CMin = os.path.join(main_dir, "CMin.wav")
CAug = os.path.join(main_dir, "CAug.wav")

CSMaj = os.path.join(main_dir, "C#Maj.wav")
CSMin = os.path.join(main_dir, "C#Min.wav")
CSAug = os.path.join(main_dir, "C#Aug.wav")

DMaj = os.path.join(main_dir, "DMaj.wav")
DMin = os.path.join(main_dir, "DMin.wav")
DAug = os.path.join(main_dir, "DAug.wav")

DSMaj = os.path.join(main_dir, "D#Maj.wav")
DSMin = os.path.join(main_dir, "D#Min.wav")
DSAug = os.path.join(main_dir, "D#Aug.wav")

EMaj = os.path.join(main_dir, "EMaj.wav")
EMin = os.path.join(main_dir, "EMin.wav")
EAug = os.path.join(main_dir, "EAug.wav")

FMaj = os.path.join(main_dir, "FMaj.wav")
FMin = os.path.join(main_dir, "FMin.wav")
FAug = os.path.join(main_dir, "FAug.wav")

FSMaj = os.path.join(main_dir, "F#Maj.wav")
FSMin = os.path.join(main_dir, "F#Min.wav")
FSAug = os.path.join(main_dir, "F#Aug.wav")

GMaj = os.path.join(main_dir, "GMaj.wav")
GMin = os.path.join(main_dir, "GMin.wav")
GAug = os.path.join(main_dir, "GAug.wav")

GSMaj = os.path.join(main_dir, "G#Maj.wav")
GSMin = os.path.join(main_dir, "G#Min.wav")
GSAug = os.path.join(main_dir, "G#Aug.wav")

AMaj = os.path.join(main_dir, "AMaj.wav")
AMin = os.path.join(main_dir, "AMin.wav")
AAug = os.path.join(main_dir, "AAug.wav")

ASMaj = os.path.join(main_dir, "A#Maj.wav")
ASMin = os.path.join(main_dir, "A#Min.wav")
ASAug = os.path.join(main_dir, "A#Aug.wav")

BMaj = os.path.join(main_dir, "BMaj.wav")
BMin = os.path.join(main_dir, "BMin.wav")
BAug = os.path.join(main_dir, "BAug.wav")


class Sound_Class():
  def __init__(self):
    pass
  def Start_Sound(self):
    Start = os.path.join(main_dir, "Start.wav")
    winsound.PlaySound(Start, winsound.SND_FILENAME)

  def End_Sound(self):
    End = os.path.join(main_dir, "End.wav")
    winsound.PlaySound(End, winsound.SND_FILENAME)

  def Back_Button(self):
    Back = os.path.join(main_dir, "Back.wav")
    winsound.PlaySound(Back, winsound.SND_FILENAME)

  def Play_func(self, Chords):
    for line in Chords.splitlines():
    ##major chords
      if line == "C Major":
        winsound.PlaySound(CMaj, winsound.SND_FILENAME)
      elif line == "C# Major":
        winsound.PlaySound(CSMaj, winsound.SND_FILENAME)        
      elif line == "D Major":
        winsound.PlaySound(DMaj, winsound.SND_FILENAME)
      elif line == "D# Major":
        winsound.PlaySound(DSMaj, winsound.SND_FILENAME)
      elif line == "E Major":
        winsound.PlaySound(EMaj, winsound.SND_FILENAME)
      elif line == "F Major":
        winsound.PlaySound(FMaj, winsound.SND_FILENAME)
      elif line == "F# Major":
        winsound.PlaySound(FSMaj, winsound.SND_FILENAME)
      elif line == "G Major":
        winsound.PlaySound(GMaj, winsound.SND_FILENAME)
      elif line == "G# Major":
        winsound.PlaySound(GSMaj, winsound.SND_FILENAME)
      elif line == "A Major":
        winsound.PlaySound(AMaj, winsound.SND_FILENAME)
      elif line == "A# Major":
        winsound.PlaySound(ASMaj, winsound.SND_FILENAME)
      elif line == "B Major":
        winsound.PlaySound(BMaj, winsound.SND_FILENAME)

    #minor chords
      elif line == "C Minor":
        winsound.PlaySound(CMin, winsound.SND_FILENAME)
      elif line == "C# Minor":
        winsound.PlaySound(CSMin, winsound.SND_FILENAME)
      elif line == "D Minor":
        winsound.PlaySound(DMin, winsound.SND_FILENAME)
      elif line == "D# Minor":
        winsound.PlaySound(DSMin, winsound.SND_FILENAME)
      elif line == "E Minor":
        winsound.PlaySound(EMin, winsound.SND_FILENAME)
      elif line == "F Minor":
        winsound.PlaySound(FMin, winsound.SND_FILENAME)
      elif line == "F# Minor":
        winsound.PlaySound(FSMin, winsound.SND_FILENAME)
      elif line == "G Minor":
        winsound.PlaySound(GMin, winsound.SND_FILENAME)
      elif line == "G# Minor":
        winsound.PlaySound(GSMin, winsound.SND_FILENAME)
      elif line == "A Minor":
        winsound.PlaySound(AMin, winsound.SND_FILENAME)
      elif line == "A# Minor":
        winsound.PlaySound(ASMin, winsound.SND_FILENAME)
      elif line == "B Minor":
        winsound.PlaySound(BMin, winsound.SND_FILENAME)

      #AUG CHORDS
      elif line == "C Aug":
        winsound.PlaySound(CAug, winsound.SND_FILENAME)
      elif line == "C# Aug":
        winsound.PlaySound(CSAug, winsound.SND_FILENAME)
      elif line == "D Aug":
        winsound.PlaySound(DAug, winsound.SND_FILENAME)
      elif line == "D# Aug":
        winsound.PlaySound(DSAug, winsound.SND_FILENAME)
      elif line == "E Aug":
        winsound.PlaySound(EAug, winsound.SND_FILENAME)
      elif line == "F Aug":
        winsound.PlaySound(FAug, winsound.SND_FILENAME)
      elif line == "F# Aug":
        winsound.PlaySound(FSAug, winsound.SND_FILENAME)
      elif line == "G Aug":
        winsound.PlaySound(GAug, winsound.SND_FILENAME)
      elif line == "G# Aug":
        winsound.PlaySound(GSAug, winsound.SND_FILENAME)
      elif line == "A Aug":
        winsound.PlaySound(AAug, winsound.SND_FILENAME)
      elif line == "A# Aug":
        winsound.PlaySound(ASAug, winsound.SND_FILENAME)
      elif line == "B Aug":
        winsound.PlaySound(BAug, winsound.SND_FILENAME)
        


