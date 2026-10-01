resolutions = [2140,1920,1366]

for resolution in resolutions:
    scrnx1 = int(resolution*0.03)
    scrny1 = int(resolution*0.03)
    scrnx2 = int(resolution*0.96)
    scrny2 = int(resolution*0.37)
    scrnw = scrnx2 - scrnx1
    scrnh = scrny2 - scrny1
    print(resolution,": x1:",scrnx1)
    print(resolution,": y1:",scrny1)
    print(resolution,": x2:",scrnx2)
    print(resolution,": y2:",scrny2)
