import os

def override(df_dict, SOL):

    currentpatn = os.path.abspath(__file__)
    rootpath = os.path.dirname(currentpatn)
    zz = rootpath + "/config/"
    SOL = SOL[0]

    layers = {
            '0': 'Dose(ml/cm^2)',
            '1': 'SC_thickness',
            '2': 'VE_thickness',
            '3': 'DE_thickness',
            '4': 'Sink_thickness'
              }
    with open(zz+'Caffeine_CE.cfg', 'r') as rf:
        with open(zz+'Caffeine_CE_copy.cfg', 'w') as wf:
            for line in rf:
                line = line.split()
                if not line or line[0]=='#':
                    continue
                if line[0] == 'COMP':
                    layer = layers[line[1]]
                    if df_dict[layer][0]:
                        if line[1] == '0':
                            line[2] = str(float(df_dict[layer][0])*0.01)
                            #line[2] = 100e-6
                        else:
                            line[2] = df_dict[layer][0]
                elif line[0] == 'CHEM_MW':
                    if df_dict[line[0]][0]:
                        line[1] = df_dict['CHEM_MW'][0]
                        line[1] = str(line[1])            
                elif line[0] == 'SOLUBILITY_VH':
                        line[1] = str(SOL)
                elif line[0] == 'CHEM_KOW':
                    if df_dict[line[0]][0]:
                        line[1] = df_dict['CHEM_KOW'][0]
                        line[1] = str(line[1])
                elif line[0] == 'Chem_VP':
                    if df_dict[line[0]][0]:
                        line[1] = df_dict['Chem_VP'][0]
                        line[1] = str(line[1])
                elif line[0] == 'KW_VH':
                    if df_dict[line[0]][0]:
                        line[1] = df_dict['KW_VH'][0]
                        line[1] = str(line[1])
                elif line[0] == 't_end':
                    if df_dict['t_end(h)'][0]:
                        line[1] = df_dict['t_end(h)'][0]+'*3600'
                elif line[0] == 'Nsteps':
                    if df_dict['t_end(h)'][0]:
                        nstep = (int(df_dict['t_end(h)'][0])*5)+1
                        line[1] = str(nstep)
                elif line[0] == 'INFINITE_VH':
                    if df_dict['product_type'][0] and df_dict['product_type'][0] == 'in-vitro(infinite does)':
                        line[1] = '1'
                elif line[0] == 'CHEM_DENSITY':
                    if df_dict[line[0]][0]:
                        line[1] = df_dict['CHEM_DENSITY'][0]
                        line[1] = str(line[1])
                elif line[0] == 'CHEM_NONION':
                    if df_dict[line[0]][0]:
                        line[1] = df_dict['CHEM_NONION'][0]
                        line[1] = str(line[1])
                elif line[0] == 'CHEM_UNBND':
                    if df_dict[line[0]][0]:
                        line[1] = df_dict['CHEM_UNBND'][0]
                        line[1] = str(line[1])
                line = ' '.join(line) + '\n'
                wf.write(line)

