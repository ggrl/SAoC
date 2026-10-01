import tkinter as tk

#local dep
import programs.puller_team
import configs.config_priv as conf

'''
Fight-Bar:5
Buff-Bar: 6
Utility-Bar: 7
'''

# ----- Configuration -----#

team = conf.team

#--------------------------#

def send_command(command):
    for x in conf.team:
         if conf.team[x][1]:
            programs.puller_team.send_forget(command, team[x][0])
         else:
             print("not sent")   


def main():
    #--------- GUI ---------#
    root = tk.Tk()
    root.title("manual drive")
    root.attributes("-topmost", True)
    root.resizable(False, False)
    root.overrideredirect(True)
    tk.Button(root, text="X", command=root.destroy).pack()

    def start_move(event):
        root.x = event.x
        root.y = event.y


    def move(event):
        x = root.winfo_x() + event.x - root.x
        y = root.winfo_y() + event.y - root.y
        root.geometry(f"+{x}+{y}")


    dragbar = tk.Frame(root, height=15)
    dragbar.pack(fill="x")

    dragbar.bind("<Button-1>", start_move)
    dragbar.bind("<B1-Motion>", move)


    buttons = [
    ("FORMATION", lambda: send_command("formation")),
    ("FIGHT", lambda: send_command("fight")),
    ("WAIT", lambda: send_command("wait")),
    ("SIT", lambda: send_command("sit")),
    ("BUFF", lambda: send_command("buff")),
    ("STICK", lambda: send_command("stick")),
    ("SPRINT", lambda: send_command("sprint")),
    ("SPREAD", lambda: send_command("spread")),
    ("START", lambda: send_command("spread")),
]

    for text, function in buttons:
        tk.Button(
            root,
            text=text,
            command=function,
            width=20
        ).pack(pady=5)

    root.mainloop()