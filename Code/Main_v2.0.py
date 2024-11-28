"""
===============================================================================
Project Name: GPS Data Display on OLED
File Name: Main_v2.0.py
Description: This script reads GPS data from a UART-connected GPS module, parses 
             the data using MicropyGPS, and displays it on an SH1106 OLED screen. 
             The displayed information includes time, date, latitude, longitude, 
             altitude, number of satellites, and horizontal dilution of precision (HDOP).

Authors: 
  - Guilherme Brito
  - Henrique Silva
  - João Santos

Version: 2.0
Date Created: 14-11-2024
Last Modified: 21-11-2024

Parameters:
  - I2C Pins: SCL = GP22, SDA = GP21
  - UART Pins: TX = GP17, RX = GP16
  - OLED Contrast: 80%
  - GPS Baud Rate: 9600
  - Display Refresh Interval: 1 second

Usage:
  - Ensure the SH1106 OLED display and GPS module are connected as per the pin 
    configuration.
  - Upload the script to a microcontroller and monitor the OLED for GPS data.
  - Exit the program with Ctrl+C.

Dependencies:
  - machine (for I2C and UART)
  - sh1106 (OLED display driver)
  - libGPS (Adaptation of the MicropyGPS for GPS parsing)

Notes:
  - This code is optimize for ESP32
  - See documentation for connections between the three 

===============================================================================
"""

import machine
from machine import I2C, Pin
from sh1106 import SH1106_I2C
from time import sleep
from libGPS import MicropyGPS

# Constants
I2C_SCL_PIN = 22  # Pin for I2C clock line
I2C_SDA_PIN = 21  # Pin for I2C data line
I2C_FREQ = 100_000  # Frequency for I2C communication in Hz
UART_TX_PIN = 17  # Pin for UART TX
UART_RX_PIN = 16  # Pin for UART RX
UART_BAUDRATE = 9600  # Baud rate for UART communication
OLED_CONTRAST = 80  # Contrast setting for the OLED display (0-255)
DISPLAY_REFRESH_INTERVAL = 1  # Interval for refreshing the display in seconds

# Function: initialize_display
# Description: Initializes the OLED display via I2C.
# Returns: The initialized OLED object.
# Raises: Exception if the I2C or OLED initialization fails.
def initialize_display():
    """
    Set up the I2C bus and OLED display.
    """
    try:
        # Initialize I2C bus
        i2c = I2C(0, scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN), freq=I2C_FREQ)
        # Initialize OLED display
        oled = SH1106_I2C(i2c)
        oled.contrast(OLED_CONTRAST)
        return oled
    except Exception as e:
        print(f"Error initializing OLED: {e}")
        raise

# Function: update_display
# Description: Updates the OLED display with the given GPS data.
# Parameters:
#   oled (SH1106_I2C): The OLED display object.
#   gps_data (dict): Dictionary containing GPS data (time, date, lat, long, etc.).
def update_display(oled, gps_data):
    """
    Refreshes the OLED display with new GPS data.
    """
    oled.fill(0)  # Clear the screen

    # Display labels
    oled.text("Time:", 0, 0) #(text, x position, y position)
    oled.text("Date:", 0, 9)
    oled.text("Lat:", 0, 18)
    oled.text("Long:", 0, 27)
    oled.text("Altitude:", 0, 36)
    oled.text("N Satellites:", 0, 45)
    oled.text("HDOP:", 0, 54)

    # Display GPS data
    oled.text(f"{gps_data['time']}", 38, 0)  # Truncate time to HH:MM:SS
    oled.text(f"{gps_data['date']}", 38, 9)
    oled.text(f"{gps_data['latitude'][:12]}", 30, 18)
    oled.text(f"{gps_data['longitude'][:12]}", 38, 27)
    oled.text(f"{gps_data['altitude']}", 70, 36)
    oled.text(f"{gps_data['satellites']}", 103, 45)
    oled.text(f"{gps_data['hdop']}", 38, 54)
    oled.show()  # Update the OLED screen 


# Function: parse_gps_data
# Description: Parses raw GPS data from the MicropyGPS object into a dictionary.
# Parameters:
#   my_gps (MicropyGPS): The MicropyGPS object handling GPS data parsing.
# Returns: Dictionary containing parsed GPS data.
def parse_gps_data(my_gps):
    """
    Extracts GPS data from the MicropyGPS object and formats it.
    """
    return {
        'time': my_gps.timestamp,  # Format time as HH:MM:SS
        'date': my_gps.date_string('s_dmy'),  # Date in DD/MM/YYYY format
        'latitude': my_gps.latitude_string(),  # Latitude in degrees/minutes/seconds
        'longitude': my_gps.longitude_string(),  # Longitude in degrees/minutes/seconds
        'altitude': str(my_gps.altitude),  # Altitude in meters
        'satellites': str(my_gps.satellites_in_use),  # Number of satellites in use
        'hdop': str(my_gps.hdop),  # Horizontal Dilution of Precision
    }

# Function: main
# Description: Main function to initialize components and handle GPS data processing and display updates.
def main():
    """
    The main program loop. Initializes the OLED display and GPS module, then continuously
    updates the display with parsed GPS data.
    """
    # Initialize the OLED display
    oled = initialize_display()

    # Instantiate the GPS parser
    my_gps = MicropyGPS()

    # Initialize UART for GPS communication
    gps_serial = machine.UART(2, baudrate=UART_BAUDRATE, tx=UART_TX_PIN, rx=UART_RX_PIN)
    
    print("System initialized. Press Ctrl+C to exit.")
    try:
        while True:
            gps_data_available = False
            # Read GPS data from the UART interface
            while gps_serial.any():
                data = gps_serial.read()
                for byte in data:
                    # Update GPS parser with each byte
                    if my_gps.update(chr(byte)) is not None:
                        gps_data_available = True
            
            # If new GPS data is available, process and display it
            if gps_data_available:
                gps_data = parse_gps_data(my_gps)
                update_display(oled, gps_data)
                
                # Print GPS data line by line for readability
                print("\n--- GPS Data ---")
                for key, value in gps_data.items():
                    # Print GPS data line by line for readability
                    print("\n--- GPS Data ---")
                    print(f"Time: {gps_data['time']}")
                    print(f"Date: {gps_data['date']}")
                    print(f"Latitude: {gps_data['latitude']}")
                    print(f"Longitude: {gps_data['longitude']}")
                    print(f"Altitude: {gps_data['altitude']} meters")
                    print(f"Satellites: {gps_data['satellites']}")
                    print(f"HDOP: {gps_data['hdop']}")
                print("-----------------")
            
            sleep(DISPLAY_REFRESH_INTERVAL)  # Delay to control refresh rate
    except KeyboardInterrupt:
        print("Program stopped. Exiting...")
        oled.poweroff()  # Turn off the OLED display

# Entry point for the script
if __name__ == "__main__":
    main()
