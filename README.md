# Final_Project
 Final Project for CS162

**Design**

How to use: 

This program creates graphical interface displaying 3 device buttons. Those devices when clicked on will cause an event output at the terminal saying "[device] clicked!" 
There are 3 more buttons that are tied respectively to a device. These trigger specific methods for the device and are displayed in the terminal.
There is also an entry box along with an "Enter" button and a "Read File" button. Entering text into the entry box and then hitting the enter button will write the inputted text to a file (message.txt). Clicking the read file button opens the file and outputs the contents to the terminal.

**This program demonstrates the following**

***Variables, Conditionals, Loops, and Collections*** - All files

***Code organization (formatting, identifiers, placement of definitions)*** - All files

***Code decomposition (functions, classes, methods, and modules)*** - All files

***An understanding of design (including hierarchy of aggregate objects and an inheritance tree)***

Inheritance tree:

                        Device
                /          |          \
            Light      Thermostat       Camera
                                            \
                                        PowerOnError


***User IO, file IO, and input validation*** - main.py : write_file(), read_file()

***Recursion*** - camera.py : shutter_pictures()

***GUI components and event driven programming*** - main.py

***Exceptions*** - light.py, thermostat.py

***Inheritance*** - device.py (inheritted by light.py, camera.py, thermostat.py)