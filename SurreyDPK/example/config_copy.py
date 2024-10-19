import os

def override():

    currentpatn = os.path.abspath(__file__)
    rootpath = os.path.dirname(currentpatn)
    zz = rootpath + "/config/"

    with open(zz+'Caffeine_CE_copy.cfg', 'r') as rf:
        with open(zz+'Caffeine_CE_first_hour.cfg', 'w') as wf:
            for line in rf:
                line = line.split()
                if not line or line[0]=='#':
                    continue
                elif line[0] == 't_end':
                    line[1] = '1'+'*3600'
                elif line[0] == 'Nsteps':
                    nstep = 20+1
                    line[1] = str(nstep)
                line = ' '.join(line) + '\n'
                wf.write(line)