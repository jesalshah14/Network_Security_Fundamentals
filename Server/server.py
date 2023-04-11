import socket

# class ConnectedClient:
#     def __init__(self) -> None:
#         self.socket
#         self.address:str

class Server:
    def __init__(self) -> None:
        self.__create_server()
        # self.socket
        # self.host:str = ""
        # self.port :int = 0
        
    
    def __create_server(self) -> None:
        try:  
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.host = socket.gethostname()
            self.port = 12345
            self.socket.bind((self.host, self.port))  
        except ValueError:
            print("Something went wrong and wasn't possible to be a server")
        
    
    def connect_client(self):   
        try:    
            self.socket.listen(1)
            print("Waiting for a client to connect...")
            client = self.socket.accept()      
            return client
        except ValueError:
            print("Something went wrong. No client connected")
        
