import socket
import threading
import json  # Assuming the data format is JSON, but adjust as necessary

class MevoPlusConnector:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.connection = None
        self.listeners = []  # Listeners for shot data events

    def connect(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.address, self.port))
        print("Connected to Mevo+ launch monitor.")
        threading.Thread(target=self.listen_for_data, daemon=True).start()

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from Mevo+ launch monitor.")

    def listen_for_data(self):
        try:
            while self.connection:
                data = self.connection.recv(1024)  # Adjust buffer size as needed
                if data:
                    shot_data = json.loads(data.decode('utf-8'))  # Example parsing, adjust as necessary
                    self.trigger_shot_event(shot_data)
        except Exception as e:
            print(f"Error receiving data: {e}")

    def trigger_shot_event(self, shot_data):
        for listener in self.listeners:
            listener(shot_data)

    def add_shot_listener(self, listener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_shot_listener(self, listener):
        if listener in self.listeners:
            self.listeners.remove(listener)
