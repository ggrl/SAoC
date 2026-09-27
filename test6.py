import puller_team

while True:
    option = input('choose option: ')
    if option == 'regg' or option == 'start':
        puller_team.send_wait(option, puller_team.team['heal'])
    else:
        puller_team.send_forget(option, puller_team.team['heal'])    