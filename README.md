# MevoPlus Connector

This project provides a Python-based solution for connecting to a Mevo+ launch monitor over WiFi using sockets, enabling real-time collection and processing of shot data.

## Features

- Establishes a socket connection to Mevo+ launch monitor.
- Listens for shot data and raises an event upon receiving new data.
- Provides a framework for extending functionality and integrating with other systems.

## Requirements

- Python 3.6+
- PySide6 (for GUI components, if needed)

## Installation

1. Clone this repository or download the ZIP file.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the application:

```python
python MevoPlusApp.py
```

Ensure you adjust the IP address and port to match your Mevo+ launch monitor's configuration.

### Starting the App via Python Terminal

You can also start the app via the Python terminal with the following steps:

1. Open your terminal or command prompt.
2. Navigate to the directory containing the `MevoPlusApp.py` file.
3. Start the Python interactive shell by typing `python` or `python3`.
4. Execute the following Python code:

```python
from MevoPlusApp import MevoPlusApp

# Replace '192.168.1.1' with the IP address of your Mevo+ launch monitor
# and '12345' with the port number it uses for connections.
app = MevoPlusApp('192.168.1.1', 12345)
app.run()
```

This will initiate the connection to your Mevo+ launch monitor and start listening for shot data. The application will run until you terminate it manually (e.g., by pressing `Ctrl+C` in the terminal).

## Extending the Application

The application can be extended by modifying `MevoPlusApp.py` and `MevoPlusConnector.py` to add additional functionality or integrate with other systems.
