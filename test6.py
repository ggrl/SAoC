import puller_team

while True:
    option = input('choose option: ')
    if option == 'regg':
        puller_team.send_wait('regg', puller_team.team['heal'])
    else:
        puller_team.send_forget(option, puller_team.team['heal'])    