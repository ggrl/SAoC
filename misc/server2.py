import socket
import threading
import time


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


def def_c(stop_event):
        print("C läuft")
        time.sleep(5)
        print("C läuft")
        time.sleep(3)
        print("C beendet")
        # Arbeit von C


functions = {
    "a": def_a,
    "b": def_b,
    "c": def_c
}


current_thread = None
stop_event = None


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(1)

print("|--------- Listening --------|")


while True:

    conn, addr = server.accept()

    data = conn.recv(1024)
    message = data.decode().strip()

    conn.close()

    if message in functions:

        # bisherige Funktion stoppen
        if stop_event:
            stop_event.set()

        # neuen Stop-Event erzeugen
        stop_event = threading.Event()

        # neue Funktion starten
        current_thread = threading.Thread(
            target=functions[message],
            args=(stop_event,)
        )

        current_thread.start()