# DE2-Project-GPS-Tracker
Resume:
The document provides a detailed description of the GPS Tracker project, beginning with identifying the team members and their respective responsibilities. Each team member is introduced with a brief explanation of their role in the project's development, such as hardware design, software implementation, or component integration.

It then provides a detailed explanation of the hardware, describing the implemented system and the components used, such as the GPS module and environmental sensors. This section also includes block diagrams, clearly illustrating the system's architecture and the connections between the various components.

In the software section, the algorithms developed for the system's operation are presented, complemented by flowcharts to clarify the logic behind the operations. This section also provides direct links to the source code files and an explanation of the libraries and modules used in the development, highlighting the technical decisions made.

The document also includes a user guide for the application, describing the steps required to configure and operate the system. Additionally, photographs of the device in operation are included to illustrate the achieved results and demonstrate its practical utility.

Finally, the document concludes with a list of references consulted during the project development, such as technical articles, tutorials, or manuals, as well as the online tools used, such as circuit design software or platforms for analysis and development. This information collection consolidates the project, presenting it, comprehensively, and professionally.

Objetive: 
GPS-based environmental sensor data logger. The system integrates GPS functionality for location tracking and environment sensor(s) to capture data related to environmental conditions. 
The project aims to log and display sensor data and provide the capability to export the collected information for analysis.

# Team Members - Group 3
This chapter outlines the distribution of roles and responsibilities among the members of the project team, ensuring clarity in task allocation and efficient collaboration throughout the development process. Each team member contributed to the project by focusing on specific aspects while also working collectively on the core functionalities.

•	Henrique Silva was responsible for the development and integration of the monitor library, as well as contributing significantly to the main code implementation.

•	Guilherme Brito took charge of the project documentation, ensuring that all processes and results were recorded, while also playing a vital role in the main code development.

•	João Santos focused on the design and implementation of the GPS library, ensuring seamless communication with the GPS module, and collaborated on the main code development as well.

-------------------------------
Group 3 - BPA-DE2:
- Henrique Silva --> Responsible for Monitor library and main code
- Guilherme Brito --> Responsible for Documentation and main code
- João Santos -->  Responsible for GPS library and main code
-------------------------------

# Hardware description

The hardware implementation of the project is built around a set of key components, carefully selected to ensure functionality and integration. The system uses an ESP32 microcontroller as the central processing unit, providing robust computing power and wireless connectivity. A NEO-6M GPS module is used for location tracking, offering reliable and accurate positioning data. 

To display real-time information, the setup incorporates an OLED screen, which allows for a clear and compact user interface. The components are interconnected using jumper wires on a breadboard, enabling a modular and easily modifiable design during development.

![ESP32-NEO-GPS-Circuit_fritzing](https://github.com/user-attachments/assets/7546ce28-0553-4b24-b391-57d4fe78cc1e)

As we can see in the previous figure, the diagram illustrates the hardware system centred on the ESP32, showing the connections to peripheral modules and the power supply. The ESP32 is presented at the center, acting as the main unit that manages communication and electrical power distribution to the connected devices.

In the upper right corner, the OLED Screen module is depicted, receiving power and data through four connections to the ESP32. The power supply is provided via the VCC and GND pins, while the SDA and SCK pins are used for communication, configured through the I2C protocol. These connections are color-coded, with blue wires for communication signals and red and black wires for power and ground, respectively.

In the lower right corner, the NEO-6M GPS module is shown. This module communicates with the ESP32 by UART, using the RXD and TXD pins which are connected by yellow wires. The GPS module is powered by the ESP32’s 3V3 pin, with the power line shown in red, and is grounded via a black wire. Additionally, the GPS module has a PPS pin, which is not directly used in this diagram.

At the bottom centre, a block representing the DC Power Supplies is displayed. This component provides energy to the ESP32.

The diagram uses directional arrows and color coding to highlight the flow of data and power within the system. Red and black lines represent power (positive and ground), while yellow and blue lines indicate logical communication paths between the modules. This schematic provides a clear overview of the physical and functional interconnections, emphasizing how the ESP32 serves as the core to manage both power and data signals across the devices.

# Software description

Modules Used in the Project:
1. **machine**
    - Used to interface with hardware components like I2C and UART for communication with the OLED and GPS modules.
2. **sh1106**
    - A library created in class for controlling SH1106-based OLED displays via the I2C interface.
3. **time**
    - Used for implementing delays (e.g., refreshing the display every second).
4. **libGPS (MicropyGPS)**
    - A library for parsing NMEA data from the GPS module and extracting useful information like latitude, longitude, altitude, and time.
    - Library that was adapted to have the best look for the project and for the used OLED display.

# Flowchart

![flowchart](https://github.com/user-attachments/assets/e01602de-e49c-4da2-8b25-24a69aba363b)

1. **Start**
    - Power on the system.
    - Prepare I2C and UART for communication.

2. **Initialize I2C for OLED display.**
    - Set up I2C pins (SCL and SDA) and frequency.
    - Try to Initialize the OLED Display.
        - If successful, proceed to next step.
        - If initialization fails, display an error and stop program.

3. **Initialize GPS Module**
    - Set up UART pins (TX and RX) and baud rate.
    - Create a MicropyGPS object to parse incoming data.

4. **Main Loop**
    - **Check for incoming GPS Data**
        - Monitor the UART interface for available data.
        - If no data is available, wait and check again.
        - If data is available:
            - Read the data byte by byte.
            - Feed each byte to MicropyGPS for parsing.
    - **Parse GPS Data**
        - Extract the parameters values from MicropyGPS
    - **Update OLED Display**
        - Clear the OLED screen
        - Write the parsed GPS data to the screen with appropriate labels.
        - Refresh the display to show the new data.
    - **Print GPS Data to Console**
        - Display parsed data in a simple format in the terminal for easy reading
    - **Wait for Refresh Interval**
        - Pause execution for a predefined time before starting the next loop iteration.


5. **Check for Exit Condition**
    - Monitor for a keyboard interrupt (Ctrl + C).
        - If no interrupt is detected, return to Step 4.
        - If an interrupt is detected, proceed to the next step.

6. **Shutdown**
    - Power off the OLED Display.
    - End the program.

7. **Stop**

# Instructions
1. Connect the jumper in order to connect all 3 devices (ESP32, GPS Module and OLED Display) as shown in the figure below.

![Circuit_Diagram](https://github.com/user-attachments/assets/455a3f9e-e92e-44d7-beff-9a5b6a6256fd)

    - Obtaining something like this:

![Circuit_Display_OFF](https://github.com/user-attachments/assets/bbf682d3-a843-4b10-9210-2700e9cbede7)

2. After all the connections made, connect the USB to your computer and your ESP32 and upload **sh1106** and **libGPS** modules to the ESP32 memory.
    - sh1106 responsible for OLED Display functions
    - libGPS responsible for collect data from GPS's

3. Once the modules are uploaded with the application **Thonny** or one look a like that can work with the ESP32 open the main code **Main_v2.0.py** and run it.

NOTES:

1. The GPS Module can take a few seconds or minutes to start detecting Satellites.

2. In case you are inside a building and unable to connect to Satellites, try to move close to a window or even try to go outside, for better results and more precision.

# Results (photos and videos)

The photo below shows the output on the OLED display and on the command line (Thonny), respectively.

![Display_Example](https://github.com/user-attachments/assets/0a9cdef8-e446-4a76-b4c5-342bb2cea8ad)


![Thonny_Output](https://github.com/user-attachments/assets/a2fcac66-02db-40ed-afb0-74726bfa5f5b)

This videos show the code running and both the available outputs, OLED Display Output and Command Line Output, respectively.

https://github.com/user-attachments/assets/5a955ce9-9638-4b4e-9098-6e26349ae57e


https://github.com/user-attachments/assets/b2f835c3-f0e8-4052-82ba-102601ce1336


We can notice a difference in the outputs on the Dislpay and on Thonny, this was a group decision, once the OLED Display has a limited space we decided to only insert a reduce number of the parameters and once the command line doesn't have that limit we print all the parametrs there.


# Output analysis

- **Date** -> in format DD/MM/YYYY, this parameter can be change on *Main_v2.0.py* in line 120, available formats are: 's_mdy', 's_dmy', or 'long'.
- **Time** -> in format HH:MM:SS, this parameter can be change on *libGPS.py* in line 123, here you can format manually how the times is showned.
- **Lat** (Latitude) -> Latitude displayed in short format, this format can be change on *Main_v2.0.py* in line 122, available formats are:
    Decimal Degree Minute (ddm) - 40° 26.767′ N
    Degrees Minutes Seconds (dms) - 40° 26′ 46″ N
    Decimal Degrees (dd) - 40.446° N
- **Long** (Longitude) -> Longitude displayed in short format, this format can be change on *Main_v2.0.py* in line 123, available formats are:
    Decimal Degree Minute (ddm) - 40° 26.767′ N
    Degrees Minutes Seconds (dms) - 40° 26′ 46″ N
    Decimal Degrees (dd) - 40.446° N
- **Altitude** -> Altitude relative to sea level in meters.
- **Speed** -> Speed in Km/h, this parameter can be change to mph on *Main_v2.0.py* in line 125, available formats are: 'kph' or 'mph' if mph is not specified as a function parameter then it will be displaied in kph by default (as is in used).
- **N Satellites** (Number of Satellites) -> Number of Satellites available from which is possible to collect data.
- **Position Dilution of Precision** (PDOP) -> A measure of overall GPS accuracy based on satellite geometry; lower values mean better accuracy.
- **Horizontal Dilution of Precision** (HDOP) -> Accuracy of GPS position on the horizontal plane (latitude and longitude).
- **Vertical Dilution of Precision** (VDOP) -> Accuracy of GPS position in the vertical dimension (altitude).

NOTES:

1. In some of the tests we saw that the initial accuracy it's not the best, recomending to leave it for some seconds before starting analising data.

2. The choosen format was made in order to save space on the OLED Display beeng this small.

# References and tools
1. https://randomnerdtutorials.com/micropython-esp32-neo-6m-gps
2. https://wokwi.com/projects/394218963208433665
3. https://www.robotique.tech/robotics/view-location-data-sent-by-neo-m6-gps-using-esp32-board/
