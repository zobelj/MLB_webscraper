MAXRUNS = 15

def getInningProb(inningProb, runsPerGame, hFA):
    # change R/G to R/I
    RI = runsPerGame / 9

    # define constants
    c = 0.767
    a = c * pow(RI, 2)

    # add home field advantage
    if(hFA == 1):
        RI += 0.075 / 9
    elif(hFA == -1):
        RI -= 0.075 / 9
    
    # calculate probability array
    inningProb[0] = RI / (RI + a)
    d = 1 - c * inningProb[0]
    inningProb[1] = (1 - inningProb[0]) * (1 - d)
    for i in range(2, MAXRUNS):
        inningProb[i] = inningProb[i-1] * d

def get9InnProb(inningProb):
    prob = [0] * MAXRUNS

    for n in range(MAXRUNS):
        for i1 in range(MAXRUNS, -1, -1):
            for i2 in range(MAXRUNS-i1, -1, -1):
                for i3 in range(MAXRUNS-i1-i2, -1, -1):
                    for i4 in range(MAXRUNS-i2-i3, -1, -1):
                        for i5 in range(MAXRUNS-i1-i2-i3-i4, -1, -1):
                            for i6 in range(MAXRUNS-i1-i2-i3-i4-i5, -1, -1):
                                for i7 in range(MAXRUNS-i1-i2-i3-i4-i5-i6, -1, -1):
                                    for i8 in range(MAXRUNS-i1-i2-i3-i4-i5-i6-i7, -1, -1):
                                        for i9 in range(MAXRUNS-i1-i2-i3-i4-i5-i6-i7-i8, -1, -1):
                                            if(i1+i2+i3+i4+i5+i6+i7+i8+i9 == n):
                                                prob[n] += inningProb[i1]*inningProb[i2]*inningProb[i3]*inningProb[i4]*inningProb[i5]*inningProb[i6]*inningProb[i7]*inningProb[i8]*inningProb[i9]
    return(prob)
        

team1InnProb = [0] * MAXRUNS
team2InnProb = [0] * MAXRUNS

team1GameProb = [0] * MAXRUNS
team2GameProb = [0] * MAXRUNS

RG1 = float(input("Enter team 1 R/G -> "))


getInningProb(team1InnProb, RG1, 0)


team1GameProb = get9InnProb(team1InnProb)


print(team1GameProb)
