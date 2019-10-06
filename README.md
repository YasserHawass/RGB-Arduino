# RGB-Arduino
Controlling RGB LED strips with arduino uno and python (pySerial)

So the trick is simple, you follow similar schematic like this

PS: i used n-mosfets, 470 ohms resistors between arduino and transistors, and 12k ohms resistors between gate and source
![alt text](https://github.com/YasserHawass/RGB-Arduino/blob/master/docs/RGB_LED_Strip_bb.png)


# TODO:
- Improve circuitry (maybe add pnp to the pnp to drive the mosfet)
- Turn circuit into PCB
- add backend to the the GUI, so i could control it online
  - add progressive frontend
- improve the not so friendly GUI (Especially the color select)
- improve documentation (Technical & Non technical sections)
- fix wakeMe() bugs, if not deactivated from the CLI

# Mentions:

arduino code and cie file is inspired from rodrigogarces' repo
https://github.com/rodrigogarces/Arduino-RGB-led-strip
