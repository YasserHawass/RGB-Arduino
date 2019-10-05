import serial
import time
import tkinter as tk


window = tk.Tk()
window.configure(background="gray")
window.geometry("330x80")
window.title("GG")


arduino = serial.Serial('COM3', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)  #todo auto detection for arduino UNO
print(arduino.name)         # check which port was really used

def motor_control():
    print(">>> MOTOR CTRL PROGRAM <<<\n")
    def forward():
        print("CTRL -> FORWARD + GREEN LED -> ON")
        arduino.write(b'80.80.80')

    def reverse():
        print("CTRL -> REVERSE + RED LED -> ON")
        arduino.write(b'255.80.80')

    def quit():
        print("\n** END OF PROGRAM **")
        arduino.write(b'0.0.0')
        arduino.close()
        window.destroy()

    b1 = tk.Button(window, text="FORWARD", command=forward, bg="forest green", fg="gray7", font=("Comic Sans MS", 15))

    b2 = tk.Button(window, text="REVERSE", command=reverse, bg="firebrick2", fg="ghost white", font=("Comic Sans MS", 15))

    b3 = tk.Button(window, text="EXIT", command=quit, bg="gold", fg="gray7", font=("Comic Sans MS", 15))

    b1.grid(row=1, column=0, padx=5, pady=10)
    b2.grid(row=1, column=1, padx=5, pady=10)
    b3.grid(row=1, column=2, padx=5, pady=10)

    window.mainloop()

time.sleep(2)
motor_control()


# while True:
#     try:
#         arduino.write(b'80.80.80')     # write a string
#     except (KeyboardInterrupt, EOFError):
#         print()
#         break


# arduino.close()
# ser.read_until()
# ser.close()             # close port