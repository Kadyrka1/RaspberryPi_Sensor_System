# RaspberryPi_Sensor_System
Sensor Communication with PC using python 
  <br><br/>
<img width="4000" height="3000" alt="1000118289" src="https://github.com/user-attachments/assets/20a27d95-a0f5-4966-8989-91de94b1692a" />

  
I have created two applications. First application is called M9.py
Inside this file you will see 3 main sections that govern 1 - matplotlib to plot data on the graph, 2 - main window that governs GUI and uses pyvisa to connect to the device using usb communication, and 3 - buttons that allow to connect and disconnect devices, and acquire and plot data.
UI for this project was developed using QTDesigner.
  
<img width="798" height="631" alt="Screenshot 2025-12-23 152803" src="https://github.com/user-attachments/assets/611fba12-6dfb-403c-b980-ac8381e002fd" />
  
<img width="876" height="634" alt="Screenshot 2025-12-23 152723" src="https://github.com/user-attachments/assets/d9f89002-839f-4b6b-aa84-e7918aceb802" />
  
  
Second application is named main.py and is running on RaspberryPi Pico. This code allows it to receive commands and output data. To physical pins I have connected a variable resistor that is supposed to act as a sensor (e.g. strain gauge). It is running this code:
<img width="603" height="785" alt="Screenshot 2026-04-26 135207" src="https://github.com/user-attachments/assets/8b81ca82-ab1a-41d9-96e3-2f64b276f9f3" />

