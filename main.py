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

        my_light = light.Light
        my_thermostat = thermostat.Thermostat
        my_camera = camera.Camera
        
        self.devices = [my_light().type, my_thermostat().type, my_camera().type]

        self.create_device_buttons()
        self.create_input_section()

    def create_device_buttons(self):
        # self.device_frame = tk.Frame(self.root)
        # self.device_frame.pack(pady=10)

        for device in self.devices:
            btn = tk.Button(root, text=device, command=lambda d=device: self.device_clicked(d))
            btn.pack(side=tk.LEFT, padx=5)

    def device_clicked(self, device):
        print(f"{device} clicked!")

    def create_input_section(self):
        # self.input_frame = tk.Frame(self.root)
        # self.input_frame.pack(pady=10)

        self.input_label = tk.Label(root, text="Enter a message:")
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.input_entry = tk.Entry(root)
        self.input_entry.pack(side=tk.LEFT, padx=5)

        self.enter_button = tk.Button(root, text="Enter", command=self.write_file)
        self.enter_button.pack(side=tk.LEFT, padx=5)

        self.read_button = tk.Button(root, text="Read File", command=self.read_file)
        self.read_button.pack(side=tk.LEFT, padx=5)

    def write_file(self):
        message = self.input_entry.get()
        if message:
            with open("messages.txt", "a") as file:
                file.write(message + "\n")
            self.input_entry.delete(0, tk.END)
            print("Success", "Message written to file.")
        else:
            print("Input Error", "Please enter a message.")

    def read_file(self):
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
