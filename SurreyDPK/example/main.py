import run_invitro
import sys
import matplotlib.pyplot as plt

path = "C:\\Users\\dz0004\\E2E_Unilever_project\\source_code\\SurreyDPK\\example"
path1 = "C:\\Users\\dz0004\\E2E_Unilever_project\\source_code\\SurreyDPK\\example\\simu"
sys.path.append(path)

permibility, df2, depth1, depth2, depth3, sc_conc, ve_conc, de_conc = run_invitro.compInvitro(path+'\\config\\Caffeine_CE_copy.cfg', False, path1+'./simu')
# time = df2['time']
# time = [i/3600 for i in time]
# flux_vh_sc = df2['flux_vh_sc']
# flux_sc_down = df2['flux_sc_down']
# vehicle_conc = df2['vehicle_conc']
# depth0=[0]
# print(df2['sc_conc'])
# fig = plt.figure()
# plt.plot(time[1:], flux_vh_sc[1:], '.-', label = 'flux_vh_sc')
# plt.plot(time[1:], flux_sc_down[1:], '.-', label = 'flux_sc_down')
# plt.xlabel('time (h)', fontsize=12)
# plt.ylabel('flux (mol/$\mathregular{m^2}$ s)', fontsize=12)
#
# plt.legend()
# plt.show()