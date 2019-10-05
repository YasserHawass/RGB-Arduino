import serial
import time

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

    def wakeMe():
        try:
            time.sleep(60*90*4)            #60 * 60 = 60 minutes, 60 * 90 = 90 minutes.
            while True:
                print("Heavy task!")
                arduino.write(b'255.80.80')
                time.sleep(1)
                arduino.write(b'0.0.255')
                time.sleep(1)
                arduino.write(b'255.255.255')
                time.sleep(1)
        except KeyboardInterrupt:
            print("KeyboardInterrupt has been caught.")

    def quit():
        print("BYE\n")
        arduino.write(b'0.0.0')
        arduino.close()
        window.destroy()


    b1 = tk.Button(window, text="Rose", command=rose, bg="forest green", fg="gray7", font=("Comic Sans MS", 15))
    b2 = tk.Button(window, text="Red", command=red, bg="firebrick2", fg="ghost white", font=("Comic Sans MS", 15))
    b3 = tk.Button(window, text="wake me", command=wakeMe, bg="gold", fg="gray7", font=("Comic Sans MS", 15))
    b4 = tk.Button(window, text="Color", command=colorb, bg="gold", fg="gray7", font=("Comic Sans MS", 15))
    bx = tk.Button(window, text="BYE", command=quit, bg="gold", fg="gray7", font=("Comic Sans MS", 15))

    b1.grid(row=1, column=0, padx=5, pady=10)
    b2.grid(row=1, column=1, padx=5, pady=10)
    b3.grid(row=1, column=2, padx=5, pady=10)
    b4.grid(row=1, column=4, padx=5, pady=10)
    bx.grid(row=1, column=5, padx=5, pady=10)


    window.mainloop()

time.sleep(2)
alarm()