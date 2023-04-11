import socket

class Client:
    def __init__(self) -> None:
        # self.socket
        # self.host:str = ""
        # self.port :int = 0
        self.__create_client()
    
    def __create_client(self) -> None:
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.host = socket.gethostname()
            self.port = 12345
            self.socket.connect((self.host, self.port))
            print("You are connected.")
        except ValueError:
            print("Something went wrong and wasn't possible to connect to a server")
            
            
            #testing
