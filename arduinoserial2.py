import serial
import serial.tools.list_ports
import sys

def dectect():
    
    arduino_ports = []
    available_ports = list(serial.tools.list_ports.comports())
    for port in available_ports:
        if "Arduino" in port.description or "VID:PID=2341:0043" in port.hwid:
            arduino_ports.append(port.device)
    return arduino_ports
def checks():
    print("Python "+sys.version)
    print("Available ports"+str(dectect()))

def connect(port=dectect()[0],Bud_rate=9600):
    if port==dectect()[0]:
        print("Using auto dectect may not work well !!\nIt is still suggested to use with arduino uno R3")
    return serial.Serial(port, Bud_rate)

def send(serial, data, utf="utf-8", encode=True):
    """
    Sends data over a serial connection.

    Args:
        serial (serial.Serial): The serial connection object.
        data (str): The data to be sent.
        utf (str, optional): The encoding format for the data (default is 'utf-8').
        endcode (bool, optional): Whether to encode the data (default is True).
    """
    if encode:
        encoded_data = data.encode(utf)
    else:
        encoded_data = data
    
    serial.write(encoded_data)




def read(serial,bytes=-1):
    while True:
        try:
            # Read data from the serial connection
            data = serial.readline(bytes).decode('utf-8').strip()
            
            # Do something with the received data
            print("Received data:", data)
            
        except Exception as e:
            print(f"Error reading data: {e}")

