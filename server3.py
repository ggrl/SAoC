import socket
import threading
import time
import test


def def_a(stop_event):
    while not stop_event.is_set():
        print("A läuft")
        time.sleep(5)
        # Arbeit von A


def def_b(stop_event):
    while not stop_event.is_set():
        print("B läuft")
        time.sleep(5)
        # Arbeit von B


def def_c():
    print("C läuft")
    time.sleep(5)
    print("C fertig")


functions = {
    "a": def_a,
    "b": def_b,
    "c": def_c,
    "d": test.def_a
}


current_thread = None
stop_event = None


def start_worker(command):
    global current_thread, stop_event

    # aktuellen Worker stoppen
    if current_thread and current_thread.is_alive():
        stop_event.set()
        current_thread.join()

    stop_event = threading.Event()

    current_thread = threading.Thread(
        target=functions[command],
        args=(stop_event,)
    )

    current_thread.start()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(("0.0.0.0", 5000))
server.listen(5)

print("|--------- Listening --------|")


while True:

    conn, addr = server.accept()

    try:
        command = conn.recv(1024).decode().strip()

        if command in functions:

            if command =='c':

                # aktuellen Worker stoppen
                if current_thread and current_thread.is_alive():
                        stop_event.set()
                        current_thread.join()
                
                # C synchron ausführen
                def_c()
                
                # Client informieren
                conn.sendall(b"DONE")
            else:
                start_worker(command)
        else:
            conn.sendall(b"UNKOWN")

    finally:
        conn.close()