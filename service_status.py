class service:
    def __init__(self,name, port):
        self.name = name
        self.port = port
        self.status = "stopped"

    def start(self):
        if self.status == "stopped":
            self.status = "running"
            print(f"service {self.name} is running")
        else:
            print(f"service {self.name} is already running")

    def stop(self):
        if self.status == "running":
            self.status = "stopped"
            print(f"service {self.name} has stopped")
        else:
            print(f"service {self.name} has already stopped")

srv = service("ngnix", 80)
srv.start()
srv.start()
srv.stop()
srv.stop()