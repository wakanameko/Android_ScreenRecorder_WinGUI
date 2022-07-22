import tkinter as tk
import webbrowser
from tkinter import filedialog
from tkinter import messagebox

baseGround = tk.Tk()

baseGround.geometry('500x50')
 
baseGround.title('Android_ScreenRecorder_GUI')

baseGround.resizable(width = False, height = False)

def btn_click_start():
    import subprocess
    cmd = ('adb', 'shell', 'screenrecord', '/sdcard/Rec.mp4')
    cmd = ('adb', 'pull', '/sdcard/Rec.mp4 ~/Desktop/sdcard/Rec.mp4: 1 file pulled, 0 skipped. 26.7 MB/s (22255200 bytes in 0.795s)')
    subprocess.call(cmd)

def btn_click_adb():
    webbrowser.open('https://dl.google.com/android/repository/platform-tools_r33.0.1-darwin.zip')

label1 = tk.Label(baseGround, text='このソフトウェアを使用するにはADBが必要です。').place(x=255,y=30)
button_adb = tk.Button(
    baseGround, text='Download', command=btn_click_adb).place(x= 445, y=28)

button_Record = tk.botton(
  baseGround, text='録画開始', command=btn_click_start).place(x = 10,y = 10)

label2 = tk.Label(baseGround, text='保存先').place(x= ,y= )

txt = tkinter.Entry(width=20)
txt.place(x=50, y=10)

baseGround.mainloop()
