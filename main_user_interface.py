from BeewiPy.BeewiPy import *
from Utility.BeewiSmartBulb_display import *






if __name__ == "__main__":
    MAC_ADDRESS = "C4:BE:84:EA:66:AF"       # Here you should put the MAC address of your device
    myBulb = BeewiSmartBulb(MAC_ADDRESS)    # This will create a new BeewiSmartBulb object and connect to the device


    screen = BeewiSmartBulb_display(myBulb)


