from ctypes import cdll, c_int, c_float, POINTER, byref

import os
MAXRUNS = 25

os.add_dll_directory(r'C:\\Users\\Joey Zobel\\Documents\\git_projects\\New Sim\\tangoFunctionsC.dll')
tangoFunctions1 = cdll.LoadLibrary(r'C:\\Users\\Joey Zobel\\Documents\\git_projects\\New Sim\\tangoFunctionsC.dll')


tangoFunctions1.main()

'''
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
'''


