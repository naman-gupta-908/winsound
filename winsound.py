import winsound

print("beep sound")

freq = input("enter frequency of the beep")
dur = input("Enter duration of the beep")

winsound.Beep(freq,dur)


for i in range(0, 10):    
    winsound.Beep(freq, dur)    
    freq+= 50

print("Windows question sound")

winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)
