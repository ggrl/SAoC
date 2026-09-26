import socket
import threading
import time


#local dp
import fight
import regging
import dik_keys

'''
Fight-Bar:5
Buff-Bar: 6
Utility-Bar: 7
'''

# --- Configuration ---#

resolution = '1920'
pull_weapon = 'F1'
sit_key = 'N'
pull_key = '3'
endu = False #need endu?
mana = True #need mana?
role = fight.healer_ae_team
buffcount = 5  #max: 9 buffs

#--------------------------#


functions = {
    "fight": (role,()),
    "regg": (regging.regging,(sit_key, endu, mana)),
    "buff": (regging.buffing,(buffcount)),
    "wait": (regging.wait,())
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
    function, args = functions[command]
    current_thread = threading.Thread(
        target=function,
        args=(*args, stop_event)
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

            if command =='regg':

                # stop current worker
                if current_thread and current_thread.is_alive():
                        stop_event.set()
                        current_thread.join()
                
                # regging execute synchonous
                regging.regging(sit_key)
                
                # send client
                conn.sendall(b"DONE")
            else:
                start_worker(command)
        else:
            conn.sendall(b"UNKOWN")

    finally:
        conn.close()