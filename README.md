# DE2-Project-GPS-Tracker
Objetive: 
GPS-based environmental sensor data logger. The system integrates GPS functionality for location tracking and environment sensor(s) to capture data related to environmental conditions. 
The project aims to log and display sensor data and provide the capability to export the collected information for analysis.

# Team Members
Group 3 - BPA-DE2:
- Henrique Silva --> Responsible for Monitor library and main code
- Guilherme Brito --> Responsible for Documentation and main code
- João Santos -->  Responsible for GPS library and main code

# Hardware description
(Describe your implementation and include block or circuit diagram(s).)

![ESP32-NEO-GPS-Circuit_fritzing](https://github.com/user-attachments/assets/7546ce28-0553-4b24-b391-57d4fe78cc1e)

# Software description
(Present the modules you used in the project.)
Modules Used in the Project:
1. machine
    -Used to interface with hardware components like I2C and UART for communication with the OLED and GPS modules.
2. sh1106
    -A library created in class for controlling SH1106-based OLED displays via the I2C interface.
3. time
    -Used for implementing delays (e.g., refreshing the display every second).
4. libGPS (MicropyGPS)
    -A library for parsing NMEA data from the GPS module and extracting useful information like latitude, longitude, altitude, and time.
    -Library that was adapted to have the best look for the project and for the used OLED display.

(Put *flowchats* of your algorithm(s) and direct links to source files.)
............................EM FALTA..................................

# Instructions and photos
1. Connect the jumper in order to connect all 3 devices (ESP32, GPS Module and OLED Display) as shown in the figure below.

https://github.com/JoaoSantos2001/DE2-Project-GPS-Tracker/blob/main/Images/Circuit_Diagram.jpg?raw=true

-Obtaining something like this:

----------------------------------------FOTO MONTAGEM-------------------------------------------------

2. After all the connections made, connect the usb to your computer and your ESP32 and upload *sh1106* and *libGPS* modules to the ESP32 memory.
    -sh1106 Responsible for OLED Display functions
    -libGPS Responsible for collect data from GPS's

3. Once the modules are uploaded with the application *Thonny* or one look a like that can work with the ESP32 open the main code *Main_v2.0.py* and run it.

NOTE1: The GPS Module can take a few seconds or minutes to start detecting Satellites.

NOTE2: In case you are inside a building and unable to connect to Satellites, try to move close to a window or even try to go outside.

-Results:

The photo below shows the output on the OLED display and on the command line (Thonny), respectively.

-----------------FOTO do DISPLAY ON-------------------


https://github.com/JoaoSantos2001/DE2-Project-GPS-Tracker/blob/main/Images/Thonny_Output.jpg?raw=true

----------------FOTO OUPUT THONNY----------------------

-Working Project:

This video and the next show the code running and the both available outputs, OLED Display Output and Command Line Output, respectively.

-------------------------------------------ADICIONAR VIDEO DO ESP32----------------------------------------


--------------------------------------------ADICIONAR VIDEO DO THONNY--------------------------------------

(Describe how to use the application. Add photos or videos of your application.)

# References and tools
1. https://randomnerdtutorials.com/micropython-esp32-neo-6m-gps
2. https://wokwi.com/projects/394218963208433665
3. https://www.robotique.tech/robotics/view-location-data-sent-by-neo-m6-gps-using-esp32-board/
