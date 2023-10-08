import serial
import serial.tools.list_ports
import threading
import sys
def detect():
    """
    Detect available Arduino ports.

    Returns:
        list: List of available Arduino ports.
    """
    arduino_ports = []
    available_ports = list(serial.tools.list_ports.comports())
    for port in available_ports:
        if "Arduino" in port.description or "VID:PID=2341:0043" in port.hwid:
            arduino_ports.append(port.device)
    if arduino_ports==[]:
        print("No development board found ")
        return "None"        
    else:
        return arduino_ports

def checks():
    """
    Check available Python version and detected serial ports.
    """
    print("Python " + sys.version)
    print("Available ports: " + str(detect()))

def connect(port=detect()[0], baud_rate=9600):
    """
    Connect to a serial port.

    Args:
        port (str): The serial port to connect to.
        baud_rate (int): Baud rate for the serial connection (default is 9600).

    Returns:
        serial.Serial: The serial connection object.
    """
    if port == detect()[0]:
        print("Using auto detect may not work well!\nIt is still suggested to use with Arduino Uno R3")
    return serial.Serial(port, baud_rate)

def send_data(serial, data, utf="utf-8", encode=True):
    """
    Sends data over a serial connection.

    Args:
        serial (serial.Serial): The serial connection object.
        data (str): The data to be sent.
        utf (str, optional): The encoding format for the data (default is 'utf-8').
        encode (bool, optional): Whether to encode the data (default is True).
    """
    if encode:
        encoded_data = data.encode(utf)
    else:
        encoded_data = data
    
    serial.write(encoded_data)

def read(serial,bytes=-1):
    """
    Read data from a serial connection.

    Args:
        serial (serial.Serial): The serial connection object.
        bytes_to_read (int, optional): Number of bytes to read (default is -1 to read until newline).

    Returns:
        str: Received data from the serial connection.
    """    
    while True:
        try:
            # Read data from the serial connection
            data = serial.readline(bytes).decode('utf-8').strip()
            
            # Do something with the received data
            print("Received data:", data)
            
        except Exception as e:
            print(f"Error reading data: {e}")

def read_start(serial):
    thread = threading.Thread(target=read, args=(serial))
    thread.start()                