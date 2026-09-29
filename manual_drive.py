import tkinter as tk

#local dep
import puller_team
import configs.config_priv as conf

'''
Fight-Bar:5
Buff-Bar: 6
Utility-Bar: 7
'''

# ----- Configuration -----#

team = conf.team
grp_size = 2

#--------------------------#

def button_fight():
    for x in team:
        puller_team.send_forget('fight', team[x])


def button_wait():
    for x in team:
        puller_team.send_forget('wait', team[x])


def button_regg():
    for x in team:
        puller_team.send_wait('regg', team[x])
    

def button_buff():
    for x in team:
        puller_team.send_forget('buff', team[x])


def button_start():
    for x in team:
        puller_team.send_wait('start', team[x])

def button_stick():
    for x in team:
        puller_team.send_forget('stick', team[x])

def button_spread():
    for x in team:
        puller_team.send_forget('spread', team[x])

def button_sprint():
    for x in team:
        puller_team.send_forget('sprint', team[x]) 

def button_sit():
    for x in team:
        puller_team.send_forget('sit', team[x]) 


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
    ("FIGHT", button_fight),
    ("WAIT", button_wait),
    ("SIT", button_sit),
    ("BUFF", button_buff),
    ("STICK", button_stick),
    ("SPRINT", button_sprint),
    ("SPREAD", button_spread),
    ("START", button_start),
]

for text, function in buttons:
    tk.Button(
        root,
        text=text,
        command=function,
        width=20
    ).pack(pady=5)

root.mainloop()