import serial
import time
import datetime

import tkinter as tk
from tkinter import *

from tkinter import colorchooser
from tkcolorpicker import askcolor


window = tk.Tk()
redIntensity = IntVar()
greenIntensity = IntVar()
blueIntensity = IntVar()
window.configure(background="gray")
window.geometry("830x450")
window.title("Alarm GG")
wake = ''
wake_ = 9999 * 60 * int(time.time())


arduino = serial.Serial('COM3', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)  #todo auto detection for arduino UNO

def alarm():
    print("Alarm Ready\n")

    def colorb():
        hello = colorchooser.askcolor(initialcolor='#ff0000')
        arduino.write(('{!r}.{!r}.{!r}'.format(int(hello[0][0]),int(hello[0][1]),int(hello[0][2]))).encode('utf-8'))
        print((hello[0]))

    def rose():
        print("Rose\n")
        arduino.write(b'255.80.80')

    def red():
        print("Red\n")
        arduino.write(b'255.0.0')

    def wakeMe():       #it's buggy here
        while True:
            try:
                # print("Heavy task!")
                arduino.write(b'255.80.80')
                time.sleep(1)
                arduino.write(b'0.0.255')
                time.sleep(1)
                arduino.write(b'255.255.255')
                time.sleep(1)
            except KeyboardInterrupt:
                print("KeyboardInterrupt has been caught.")
                label.config(bg="black")
                break
            
    def set_alarm():
        global wake
        wake = wake_entry.get()
        print(wake)

    def set_alarm_():
        global wake_
        wake_ = int(wake_entry_.get()) * 60 + int(time.time())
        print(wake_)

    def quit():
        print("BYE\n")
        arduino.write(b'0.0.0')
        arduino.close()
        window.destroy()

    def tick():
        global wake
        global wake_
        current_time = time.strftime("%I:%M:%S")
        # print(dir(current_time))
        label.config(text=current_time)
        if wake == current_time[:-3]:
            label.config(bg="red")
            wakeMe()
            wake = ''
        if int(time.time()) > wake_ :
            label.config(bg="yellow")
            wakeMe()
            wake_ = 9999 * 60 * int(time.time())
        label.after(200, tick)
        
    # Funcs Buttons
    b1 = tk.Button(window, text="Rose", command=rose, bg="forest green", fg="gray7", font=("Comic Sans MS", 15))
    b2 = tk.Button(window, text="Red", command=red, bg="firebrick2", fg="ghost white", font=("Comic Sans MS", 15))
    b3 = tk.Button(window, text="wake me", command=wakeMe, bg="gold", fg="gray7", font=("Comic Sans MS", 15))
    b4 = tk.Button(window, text="Color", command=colorb, bg="gold", fg="gray7", font=("Comic Sans MS", 15))
    bx = tk.Button(window, text="BYE", command=quit, bg="gold", fg="gray7", font=("Comic Sans MS", 15))
        # Alarm Funcs
    label = Label(window, text= "Welcome", bg = "black", fg = "white", font=("Times", 50))
    wake_entry = Entry(window)
    wake_entry_button = Button(window, text="Set Alarm, 14:30", command=set_alarm)
        # Alarm Minute counter Funcs
    wake_entry_ = Entry(window)
    wake_entry_button_ = Button(window, text="Set Alarm, minutes", command=set_alarm_)

    # Grid
    b1.grid(row=1, column=0, padx=5, pady=10)
    b2.grid(row=1, column=1, padx=5, pady=10)
    b3.grid(row=1, column=2, padx=5, pady=10)
    b4.grid(row=1, column=4, padx=5, pady=10)
    bx.grid(row=1, column=5, padx=5, pady=10)

    label.grid(row=3, column=0, padx=5, pady=10)
    wake_entry.grid(row=4,column=0,padx=5,pady=10)
    wake_entry_button.grid(row=4, column=1, padx=5, pady=10)
    wake_entry_.grid(row=5,column=0,padx=5,pady=10)
    wake_entry_button_.grid(row=5, column=1, padx=5, pady=10)

    # Loop
    tick()
    window.mainloop()

time.sleep(2)
alarm()