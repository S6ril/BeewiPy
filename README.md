# BeewiPy

This is a fork of the library Beewi SmartBulb originally from [delkk0](https://github.com/delkk0/BeewiPy).

I only added a simple terminal interface to interact more easily with the lamp.

The new intefrace :

```bash
What do you want to do ?
0. Turn On/ Off
1. Set Brightness
2. Set Temperature
3. Set White
4. Set Color
5. Set Color Sequence
-----------------------
6. Exit
-----------------------
Number selected ? 
```

## How to use

In the file `main_user_interface.py` change the mac address of your light.

```python
# Here you should put the AC address of your device
MAC_ADDRESS = "C4:BE:84:EA:66:AF"       
```

If you don't know this address, you can execute the script `find_bluetooth_device.py` in the `Utility` folder. (Only test on Ubuntu 20.04 LTS).



## License
This project is licensed under the GNU General Public License v.3.

## Acknowledgements
* Thanks to [delkk0](https://github.com/delkk0/BeewiPy) for the Beewi Bulb interface in Python.
* Thanks to [IanHarvey](https://github.com/IanHarvey) for its [BluePy](https://github.com/IanHarvey/bluepy) library.
