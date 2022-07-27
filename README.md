# Battery-life-calculation-project


Project:

Creating a program for calculating the battery life of low-energy devices.

Resources:
Tkinter, Python


History:

The need for this program arose when conducting laboratory energy efficiency analyzes of IoT devices based on LoRa or ESP32.
The main requirement for them is a long service life with one battery,
during which the device must make as many work cycles as possible.
One such cycle may include measuring various indicators, processing the information 
and sending it via an information channel (RF, GSM, WiFi).
For the exact measurement of the consumption in all modes, I use the Otti program, where,
in addition to the record for Main current, there is a log file from UART.

To do this, I first wrote a short program that does only the math calculations.
Then I added data for some of the tested devices, leaving the option to choose the battery capacity.
Then I added the ability to test on new unknown devices as well.

Finally, I decided to make a user interface for other colleagues to use as well.
To make it even more useful, I added saving the measurements and saving them in a JSON file.
There is also a field for entering the self-discharge of the battery, which is taken according to the manufacturer's data.

What does it do?
As a result, when the user enters the average consumption and the period of several events,
their sequence and cyclicity, the interface displays the expected life of the battery under these conditions
and the number of cycles the device will make.