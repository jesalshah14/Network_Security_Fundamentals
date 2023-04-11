from server import Server
from RC4 import RC4Cipher

def main() -> None:
    rc4: RC4Cipher = RC4Cipher()
    key :str =""    
    key = input("Insert the key for comunication: ")

    if key !="":
        server :Server = Server()
        client_socket, client_address = server.connect_client()
        print(f"Connection from {client_address} has been established.")

        while True:
            try:
                #message got from client
                cipher = client_socket.recv(1024).decode()
                message = rc4.decryption(cipher, key)

                # if the client sends an empty message, close the connection
                if not message:
                    client_socket.close()
                    break

                # print the received message
                print(f"Client: {message}")

                # send a message back to the client
                response = input("Enter your response: ")
                response_cipher = rc4.encryption(response, key)
                client_socket.send(response_cipher.encode())
            except ValueError:
                print("Something went wrong in the connection.")
    else:
        print("The key you inform has a problem")
    

if __name__ == "__main__":
    main()
