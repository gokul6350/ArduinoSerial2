
# Arduino Serial Communication Python Library

This Python library provides a convenient interface for communicating with Arduino boards via serial communication. It allows you to detect connected Arduino boards, establish serial connections, send data, and receive data from the Arduino board.

## Features

-   **Auto Detection:** Automatically detects available Arduino (uno R3) boards connected to the computer.
-   **Connection Handling:** Easily establish serial connections with detected Arduino boards.
-   **Data Transmission:** Send data over the serial connection to Arduino boards.
-   **Data Reception:** Read data from Arduino boards and process it in real-time.
-   **Multithreading Support:** Receive data asynchronously using multithreading for responsive communication.

## Installation

To use this library, you'll need Python installed on your system. If you haven't already, download and install Python from [python.org](https://www.python.org/).
```python
pip install arduinoserial2 
```
## Usage

Here's a quick guide on how to use the library in your Python project:

### 1. Import the Library

pythonCopy code

```python 
import arduinoserial2 as as2
```

### 2. Detect Arduino Boards

pythonCopy code

```python
import arduinoserial2 as as2

as2.detect()
``` 
#### Output
```bash
Available ports: ['/dev/ttyACM0']
```

### 3. Establish Serial Connection


#### Method 1 (Recommanded)
```python 
conection=as2.connect(port='/dev/ttyACM0',baud_rate=9600)
``` 
#### Method 2 
```python 
conection=as2.connect()
``` 
##### The above code will automaticaly detect the arduino uno board and will have default baud rate `9600`
### 4. Send Data to Arduino



```python
as2.send_data(conection,"Hello Arduino ")
```

### 5. Receive Data from Arduino
```python
as2.read_start(connection)
```

### 6. Additional Features

-   **Check Python Version and Detected Ports:**
    

    
   ```python
   as2.checks()
   ``` 
    
```arduino

```
## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This library is licensed under the MIT License 