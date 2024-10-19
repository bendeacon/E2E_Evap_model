from pandas import DataFrame
import sys
path = "C:\Surrey\SurreyDPK\example"
sys.path.append(path)
import runPerm
res = runPerm.compPerm(path+'\\config\\Caffeine_CE_copy.cfg')