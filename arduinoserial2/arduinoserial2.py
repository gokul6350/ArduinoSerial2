import serial
import serial.tools.list_ports
import threading
import sys

_KNOWN_ARDUINO_VIDS = {
    0x2341,  # Arduino SA
    0x2A03,  # Arduino LLC
    0x1A86,  # CH340/CH341
    0x10C4,  # CP210x
    0x0403,  # FTDI
    0x16C0,  # Common USB-serial firmware VID
}

_PORT_KEYWORDS = (
    "arduino",
    "ch340",
    "ch341",
    "cp210",
    "ftdi",
    "usb serial",
    "usb-serial",
    "usbmodem",
    "usbser",
    "ttyacm",
    "ttyusb",
)


def _is_likely_board_port(port_info):
    if port_info.vid in _KNOWN_ARDUINO_VIDS:
        return True
    searchable = " ".join(
        str(part or "")
        for part in (
            port_info.description,
            port_info.manufacturer,
            port_info.product,
            port_info.hwid,
            port_info.name,
        )
    ).lower()
    return any(keyword in searchable for keyword in _PORT_KEYWORDS)


def detect():
    """
    Detect available Arduino ports.

    Returns:
        list: List of available Arduino ports.
    """
    arduino_ports = []
    available_ports = list(serial.tools.list_ports.comports())
    for port in available_ports:
        if _is_likely_board_port(port):
            arduino_ports.append(port.device)
    if arduino_ports:
        return arduino_ports
    fallback_ports = [port.device for port in available_ports]
    if fallback_ports:
        print("No Arduino-specific signature found. Returning available serial ports.")
        return fallback_ports
    print("No development board found ")
    return []

def checks():
    """
    Check available Python version and detected serial ports.
    """
    print("Python " + sys.version)
    print("Available ports: " + str(detect()))

def connect(port=None, baud_rate=9600, timeout=1):
    """
    Connect to a serial port.

    Args:
        port (str): The serial port to connect to.
        baud_rate (int): Baud rate for the serial connection (default is 9600).

    Returns:
        serial.Serial: The serial connection object.
    """
    if port is None:
        detected_ports = detect()
        if not detected_ports:
            raise serial.SerialException("No serial ports detected. Connect a board or pass a port explicitly.")
        port = detected_ports[0]
        print(f"Auto-detected serial port: {port}")
    return serial.Serial(port, baud_rate, timeout=timeout)

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
    thread = threading.Thread(target=read, args=(serial,), daemon=True)
    thread.start()


def main():
    checks()
