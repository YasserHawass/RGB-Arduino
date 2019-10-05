import serial
import time
import tkinter as tk

from tks.colors import ColorEntry, ColorDialog, ColorVar
from tks.color_palette import PaletteSelector
from tks.color_wheel import ColorWheel

window = tk.Tk()
window.configure(background="gray")
window.geometry("830x880")
window.title("Alarm GG")


arduino = serial.Serial('COM3', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)  #todo auto detection for arduino UNO
print(arduino.name)         # check which port was really used

def alarm():
    print("Alarm Ready\n")
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
            # quit()

    def quit():
        print("BYE\n")
        arduino.write(b'0.0.0')
        arduino.close()
        window.destroy()


    b1 = tk.Button(window, text="Rose", command=rose, bg="forest green", fg="gray7", font=("Comic Sans MS", 15))

    b2 = tk.Button(window, text="Red", command=red, bg="firebrick2", fg="ghost white", font=("Comic Sans MS", 15))

    b3 = tk.Button(window, text="wake me", command=wakeMe, bg="gold", fg="gray7", font=("Comic Sans MS", 15))

    b4 = tk.Button(window, text="BYE", command=quit, bg="gold", fg="gray7", font=("Comic Sans MS", 15))

    color_box = ColorDialog(window, "HEY")

    b1.grid(row=1, column=0, padx=5, pady=10)
    b2.grid(row=1, column=1, padx=5, pady=10)
    b3.grid(row=1, column=2, padx=5, pady=10)
    b4.grid(row=1, column=3, padx=5, pady=10)




    window.mainloop()

time.sleep(2)
alarm()