import msvcrt
import time
import datetime
import os
import pywinauto

def choiser(t2_):
    print("\n\nPress ENTER for continue")
    print("Press ESC for exit")
    print("Press Z for set counter to zero")
    print("Press C for change counter (+/-) minutes")
    inp = msvcrt.getwch()
    if (inp == chr(13)):       # Enter
        timer_loop(t2_)
    elif (inp == chr(27)):   # Esc
        print("Exit")
    elif (inp == chr(122)) or (inp == chr(1103)):  # 'z'
        timer_loop(0)
    elif (inp == chr(99)) or (inp == chr(1089)):   # 'c'
        t3 = int(input())
        t3 *= 60
        timer_loop(t2_+t3)
    else:
        choiser(t2_)

def timer_loop(last_time):
    t1 = time.time()
    while (not msvcrt.kbhit()) or (msvcrt.getwch() != chr(13)):
        t2 = time.time()-t1
        t2 = last_time + int(t2)
        t2_format = str(datetime.timedelta(seconds = t2))
        time.sleep(0.1)
        print('\r' + t2_format, end='')
    choiser(t2)

#change position and size of window
handle_ = pywinauto.findwindows.find_windows(active_only=True)[0]
app = pywinauto.application.Application().connect(handle=handle_)
dlg_spec = app.window()
dlg_spec.move_window(x=500, y=500, width=600, height=400, repaint=True)

os.system('color 37')
os.system('cls')
print("Press ENTER for start/pause")
pressedKey = msvcrt.getwch()
if pressedKey == chr(13):
    timer_loop(0)