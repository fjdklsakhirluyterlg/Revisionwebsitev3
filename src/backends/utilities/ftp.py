import socket

sock = socket.socket()  
host = socket.gethostname()  
port = 12312

sock.connect((host, port))
sock.send(b"Hello server!")

with open("Received_file", "wb") as out_file:
    print("File opened")
    print("Receiving data...")
    while True:
        data = sock.recv(1024)
        print(f"{data = }")
        if not data:
            break
        out_file.write(data)  # Write data to a file

print("Successfully got the file")
sock.close()

def send_file(filename: str, testing: bool = False) -> None:
    import socket

    port = 12312  
    sock = socket.socket()  
    host = socket.gethostname()  
    sock.bind((host, port))  
    sock.listen(5)  

    print("Server listening....")

    while True:
        conn, addr = sock.accept()  
        print(f"Got connection from {addr}")
        data = conn.recv(1024)
        print(f"Server received: {data = }")

        with open(filename, "rb") as in_file:
            data = in_file.read(1024)
            while data:
                conn.send(data)
                print(f"Sent {data!r}")
                data = in_file.read(1024)

        print("Done sending")
        conn.close()
        if testing:  
            break

    sock.shutdown(1)
    sock.close()

