import tkinter as tk
import thermostat
import camera
import light
import os

class SmartHomeGUI:
    def __init__(self, root):
        self.root = root
        self.root.minsize(400, 100)
        self.root.title("Smart Home Management System")

        self.my_light = light.Light
        self.my_thermostat = thermostat.Thermostat
        self.my_camera = camera.Camera
        
        self.devices = [self.my_light().type, self.my_thermostat().type, self.my_camera().type]
        self.attributes =[self.my_light().message, self.my_thermostat().message, self.my_camera().message]
        self.power_ons = [self.my_light.power_on, self.my_thermostat.temp_set, self.my_camera.shutter_pictures]
        self.create_device_buttons()
        self.create_attribute_buttons()
        self.create_input_section()
        

    def create_device_buttons(self):
        """Creates buttons for each device"""
        for device in self.devices:
            btn = tk.Button(root, text=device, command=lambda d=device: self.device_clicked(d))
            btn.pack(side=tk.LEFT, padx=5)      

    def create_attribute_buttons(self):
        """Creates buttons for the attributes of each device"""
        for id, attribute in enumerate(self.attributes):
            btn = tk.Button(self.root, text=attribute, command=lambda i=id: self.attribute_clicked(i))
            btn.pack(side=tk.LEFT, padx=5)
        
    def device_clicked(self, device):
        """Prints out that a device was clicked on"""
        print(f"{device} clicked!")
        
    def attribute_clicked(self, id):
        """Runs method of the current device attribute"""
        self.power_ons[id]()
    
    def create_input_section(self):
        """Creates input for writing to file, enter button, and read file button"""
        self.input_label = tk.Label(root, text="Enter a message:")
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.input_entry = tk.Entry(root)
        self.input_entry.pack(side=tk.LEFT, padx=5)

        self.enter_button = tk.Button(root, text="Enter", command=self.write_file)
        self.enter_button.pack(side=tk.LEFT, padx=5)

        self.read_button = tk.Button(root, text="Read File", command=self.read_file)
        self.read_button.pack(side=tk.LEFT, padx=5)

    def write_file(self):
        """Writes to file"""
        message = self.input_entry.get()
        if message:
            with open("messages.txt", "a") as file:
                file.write(message + "\n")
            self.input_entry.delete(0, tk.END)
            print("Success", "Message written to file.")
        else:
            print("Input Error", "Please enter a message.")

    def read_file(self):
        """Opens file"""
        if os.path.exists("messages.txt"):
            with open("messages.txt", "r") as file:
                content = file.read()
                print(content)
        else:
            print("File Error", "No file found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartHomeGUI(root)
    root.mainloop()
