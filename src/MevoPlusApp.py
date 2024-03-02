class MevoPlusApp:
    def __init__(self, address, port):
        self.connector = MevoPlusConnector(address, port)
        self.connector.add_shot_listener(self.on_shot_received)

    def on_shot_received(self, shot_data):
        print("Shot received:", shot_data)
        # Here, you can process the shot data as needed

    def run(self):
        self.connector.connect()
        try:
            while True:
                # Main application loop. This can be used to check for user input,
                # update the UI, or perform other tasks as needed.
                pass
        except KeyboardInterrupt:
            print("Shutting down...")
        finally:
            self.connector.disconnect()

# Example usage
if __name__ == "__main__":
    app = MevoPlusApp("192.168.1.1", 12345)  # Example IP and port
    app.run()
