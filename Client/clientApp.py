from client import Client
from RC4 import RC4Cipher

def main() -> None:
    rc4: RC4Cipher = RC4Cipher()
    key :str =""
    key = input("Insert the key for comunication:")

    if key !="":
        client :Client = Client()
        while True:
            try:
                # send a message to the server
                message = input("Enter your message: ")
                cipher = rc4.encryption(message,key)
                client.socket.send(cipher.encode())

                # if the message is empty, close the connection
                if not message:
                    client.socket.close()
                    break

                # receive data from the server
                response_cipher = client.socket.recv(1024).decode()
                response = rc4.decryption(response_cipher,key)
                print(f"Server: {response}")
            except ValueError:
                print("Something went wrong in the connection.")
    else:
        print("The key you inform has a problem")

    

if __name__ == "__main__":
    main()
