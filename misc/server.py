import socket
import test

def def_a():
    print("Funktion A ausgeführt")

def def_b():
    print("Funktion B ausgeführt")

def def_c():
    print("Funktion C ausgeführt")

def def_x():
    print("Funktion X ausgeführt")

functions = {
    "a": test.def_a,
    "b": def_b,
    "c": def_c,
    "x": def_x
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("0.0.0.0", 5000))
server.listen(1)

print("|-------- Listening --------|")

while True:
    conn, addr = server.accept()
    print(f"Connection from: {addr}")

    try:
        data = conn.recv(1024)
        message = data.decode().strip()
        print("Data sent: ", message)
        if message in functions:
            functions[message]()
            conn.sendall(b"Done")
        else:
            conn.sendall(b"UNKNOWN")

    except KeyboardInterrupt:
        conn.close()
        print("\nServer closed")

                

    finally:
        conn.close()
        print("Server closed")
