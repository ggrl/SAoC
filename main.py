import tkinter as tk
from tkinter import ttk
import sys

#local dp
import configs.config_priv as conf
import manual_drive
import puller_team
import solo
import support_team


programs = {
    "support_team": support_team.main,
    "puller_team": puller_team.main,
    "manual_drive": manual_drive.main
}

roles = [
    "thane_ae_team",
    "healer_ae_team",
    "bomb_ae_team"
]



def Start():
    programs[conf.program]()


#----------- GUI ------------#
def GUI():
    def config_button():
        print("|------------ Configurations -------------|")
        for name, values in team_new.items():
            ip = values["ip"].get()
            status = values["status"].get()
            conf.team[name] = (ip, status)
        print(conf.team)
        conf.program = program_cb.get()
        print(conf.program)
        conf.role = role_cb.get()
        print(conf.role)
        conf.grp_size = grpsize_sb.get()
        print(conf.grp_size)
        root.destroy()
        Start()

    
    root = tk.Tk()
    root.title("Options")
    root.attributes("-topmost", True)
    root.resizable(False, False)
    
    team_new = {}
    start_button = ttk.Button(root, text="Start", command=config_button, width=20)
    program_x = tk.StringVar(value=conf.program)
    role_x = tk.StringVar(value=conf.role)
    grpsize_x = tk.IntVar(value=conf.grp_size)
    program_cb = ttk.Combobox(root, textvariable=program_x, values=list(programs.keys()), state="readonly",width=15)
    role_cb = ttk.Combobox(root, textvariable=role_x, values=roles, state="readonly",width=15)
    grpsize_sb = ttk.Spinbox(root,textvariable=grpsize_x, from_=1, to=8, increment=1,width=5)
    plabel = ttk.Label(text="Program: ")
    rlabel = ttk.Label(text="Role: ")
    glabel = ttk.Label(text="Group Size: ")


    plabel.grid(row=1, column=0, padx=5, pady=5)
    program_cb.grid(row=1, column=1, padx=5, pady=5)
    rlabel.grid(row=2, column=0, padx=5, pady=5)
    role_cb.grid(row=2, column=1, padx=5, pady=5)
    glabel.grid(row=3, column=0, padx=5, pady=5)
    grpsize_sb.grid(row=3, column=1, padx=5, pady=5)
    start_button.grid(row=5, column=1, padx=5, pady=5)

    ip_frame = ttk.Frame(root)
    for x, name in enumerate(conf.team):
        ip = tk.StringVar(value=conf.team[name][0])
        status = tk.BooleanVar(value=conf.team[name][1])
        team_new[name] = {"ip": ip, "status": status}
        ttk.Checkbutton(ip_frame, text=name, variable=status).grid(row=x, column=0, padx=5, pady=5)
        tk.Entry(ip_frame, width=15, textvariable=ip).grid(row=x, column=1, padx=5, pady=5)
    ip_frame.grid(row=4, column=0, columnspan=2)
    if program_cb.get() == 'puller_team' or program_cb.get() == 'manual_drive':
        ip_frame.grid()
    else:    
        ip_frame.grid_remove()    


    def chose_program(event=None):
        conf.program = program_cb.get()
        if program_cb.get() == 'puller_team' or program_cb.get() == 'manual_drive':
            ip_frame.grid()
        else:    
            ip_frame.grid_remove()


    program_cb.bind("<<ComboboxSelected>>", chose_program)


    root.mainloop()

if __name__ == '__main__':
    if "-x" in sys.argv:
        Start()
    else:
        GUI()    