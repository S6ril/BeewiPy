from os import name
from BeewiPy import *
import time
from os import system, name


# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def wait_user_input():
    while True:
        try:
            selection = int(input("Number selected ? "))
            break
        except ValueError:
            print("Enter a number !!\n")

    clear()
    return selection


class BeewiSmartBulb_display:
    def __init__(self, myBulb) -> None:
        self.myBulb = myBulb
        clear()
        self.myBulb.getHWInfo()
        print("-----------------------")
        self.main_screen()

    def __del__(self):
        self.myBulb.__del__()
        print("End of programme")

    def turnOnOff(self):
        """The bulb is on when isOn() == 1 """
        if self.myBulb.isOn == 0:
            self.myBulb.turnOn()
        else:
            self.myBulb.turnOff()

        self.main_screen()

    def setBrightness(self):
        print("This method configures the brightness of the bulb in 10 steps (0 - 9).")
        print("0 being the lower brightness and 9 being the highest.")
        print("Which brightness do you want ?")
        user_input = wait_user_input()

        self.myBulb.setBrightness(user_input)
        self.main_screen()

    def setTemperature(self):
        print("This method configures the temperature of the white light when in white mode in 10 steps(0 - 9).")
        print("0 being the coolest configuration and 9 being the warmest configuration.")

        user_input = wait_user_input()

        self.myBulb.setTemperature(user_input)
        self.main_screen()

    def setWhite(self):
        print("This method configures the bulb to be in white mode, thus letting us set the desired brightness and temperature of the light.")

        self.myBulb.setWhite()
        clear()
        self.main_screen()

    def setColor(self):
        print("This method configures the bulb to be in color mode.")
        print("It uses 24-bit color to set the desired color. (0-254)")

        def user_color():
            color = -1
            while (0 > color) or (color >= 255):
                try:
                    color = int(input("Enter a color between (0 - 254) "))
                except ValueError:
                    print("Enter a number !!\n")

            return color

        print("Enter red color")
        red = user_color()
        print("Enter green color")
        green = user_color()
        print("Enter blue color")
        blue = user_color()

        print(red, blue, green)

        self.myBulb.setColor(red, green, blue)
        clear()
        self.main_screen()

    def setColorSequence(self):
        print("This method configures the bulb to be in color sequence mode.")
        print("There are 5 predefined color sequences. (0 - 4)")

        user_input = wait_user_input()

        self.myBulb.setColorSequence(user_input)
        self.main_screen()

    def main_screen(self):
        print("What do you want to do ?")
        print("0. Turn On/ Off")
        print("1. Set Brightness")
        print("2. Set Temperature")
        print("3. Set White")
        print("4. Set Color")
        print("5. Set Color Sequence")
        print("-----------------------")
        print("6. Exit")
        print("-----------------------")

        user_input = wait_user_input()

        if user_input == 0:
            self.turnOnOff()
        if user_input == 1:
            self.setBrightness()
        if user_input == 2:
            self.setTemperature()
        if user_input == 3:
            self.setWhite()
        if user_input == 4:
            self.setColor()
        if user_input == 5:
            self.setColorSequence()
