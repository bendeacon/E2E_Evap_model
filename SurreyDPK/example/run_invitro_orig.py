# -*- coding: utf-8 -*-
"""
A module containing files for calculating finite dose case
"""
import os
import numpy as np
from scipy.optimize import minimize, basinhopping, brute
import matplotlib.pyplot as plt
from importlib import reload
import pandas as pd
from pandas import read_csv
import time 
import scipy as sp
from scipy import optimize
import math
import shutil
# Using multiple processers
N_PROCESS = 8

# Import various skin
from core import chemical
reload(chemical)
from core import config
reload(config)
from core import viaepd
reload(viaepd)
from core import dermis
reload(dermis)
from core import skin_setup
reload(skin_setup)


def compInvitro(fn_conf, infinite_vh, wk_path, chem=None, sc_Kw_paras=None, sc_D_paras=None, disp=1):
    """
    Args:
        fn_conf -- the .cfg file, which gives the configuration of the simulation
        chem -- if given, it overrides the values given in fn_conf
        sc_Kw_paras -- if given, overrides the QSPR parameters to calculate Kw in stratum corneum
        sc_D_paras -- if given, overrides the QSPR parameters to calculate D in stratum corneum
    """
    b_vary_vehicle = True  #True
    b_inf_source = False
    # Read the .cfg, i.e. configuration, file to set up simulation
    _conf = config.Config(fn_conf)
    if sc_Kw_paras is not None:
        _conf.Kw_sc_paras = sc_Kw_paras
    if sc_D_paras is not None:
        _conf.D_sc_paras = sc_D_paras

    # Setup the chemical
    if chem is not None:
        _chem = chem
    else:
        _chem = chemical.Chemical(_conf)

    # Setup skin and create compartments
    _skin = skin_setup.Skin_Setup(_chem, _conf)
    if infinite_vh:
        _skin.createComps(_chem, _conf, 'ZeroConc')
    else:
        _skin.createComps(_chem, _conf, 'ZeroFlux')

    # Simulation time (in seconds) and steps

    t_start, t_end, Nsteps = [0, _conf.t_end, _conf.Nsteps]  # user defined parameters in the GUI, config template
    t_range = np.linspace(t_start, t_end, Nsteps)
    n_times=0
    for i in range(Nsteps-1):
        n_times+=1
    flux_vh_sc_list = []
    flux_sc_ve_list = []
    flux_ve_de_list = []
    flux_de_receptor_list = []
    vehicle_conc_list = []
    sc_conc_list = np.zeros([13, n_times])
    ve_conc_list = np.zeros([10, n_times])
    de_conc_list = np.zeros([10, n_times])
    total_mass_list = []
    # total mass in each compartment
    nComps = _skin.nxComp * _skin.nyComp
    mass = np.zeros([Nsteps-1, nComps])
    m_v = np.zeros([Nsteps-1, 1])
    t_list = []
    m_v_list = []
    
    #set up depth comp 1
    depth1 = [7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08,
              4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07,
              7.5e-08,
              4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08]
    depth1_1=[0]*13
    for i in range(len(depth1_1)):
        if i==0:
            depth1_1[i]=depth1[i]
        else:
            depth1_1[i]=depth1[(i-1)*3+1]+depth1[(i-1)*3+2]+depth1[(i-1)*3+3]+depth1_1[i-1]
    # set up depth comp 2
    depth2 = [1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05, 1e-05]
    depth2_2=[0]*10
    for i in range(len(depth2)):
        if i==0:
            depth2_2[i]=depth2[i]
        depth2_2[i]=depth2[i]+depth2_2[i-1]
    # set up depth comp 3
    depth3 = [2.94e-05, 2.94e-05, 2.94e-05, 2.94e-05, 2.94e-05, 2.94e-05, 2.94e-05, 2.94e-05, 2.94e-05, 2.94e-05]
    depth3_3=[0]*10
    for i in range(len(depth3)):
        if i==0:
            depth3_3[i]=depth3[i]
        depth3_3[i]=depth3[i]+depth3_3[i-1]
    # set up depth comp 4
    # depth4 = [0.124, 0.124, 0.124, 0.124, 0.124, 0.124, 0.124, 0.124, 0.124, 0.124]
    # depth4_4=[0]*10
    # for i in range(len(depth4)):
    #     if i==0:
    #         depth4_4[i]=depth4[i]
    #     depth4_4[i]=depth4[i]+depth4_4[i-1]

    for i in range(Nsteps-1):
        # Create directory to save results
        newpath = wk_path + str(t_range[i])
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        
        if b_inf_source is True:
            mass[i, :] = _skin.compMass_comps()
            m_v[1, :] = _skin.comps[0].getMass_OutEvap()
            m_all = np.insert(mass, 0, m_v[1, :]) / total_mass
            total_mass_list.append(m_all)
        else:
            if b_vary_vehicle is True:
                 mass[i, :] = _skin.compMass_comps()
                 m_v[i,0] = _skin.comps[0].getMass_OutEvap()
                 mass_evap = np.insert(mass, 0, m_v[1, :])
                 total_mass = np.sum(mass_evap)
                 m_all = mass_evap / total_mass
                 total_mass_list.append(sum(_skin.compMass_comps()+m_v[i,0])/mass[0,0])
                 #total_mass_list.append(m_all)
            else:
                mass[i, :] = _skin.compMass_comps()
                m_v[i,0] = _skin.comps[0].getMass_OutEvap()
                m_all = np.insert(mass, 0, m_v[1, :]) / total_mass
                total_mass_list.append(m_all)
        m_v_list.append(m_v)
        #print(mass, m_v, m_all, total_mass)
       
        # Save current concentrations
        for j in range(nComps):
            fn = newpath + '/comp' + str(j) + '_' + _conf.comps_geom[j].name
            _skin.comps[j].saveMeshConc(True, fn)

        flux_vh_sc = -_skin.compFlux([0, 0], 3)[0]
        flux_sc_ve = -_skin.compFlux([1, 0], 3)[0]
        flux_ve_de = -_skin.compFlux([2, 0], 3)[0]
        flux_de_receptor = -_skin.compFlux([3, 0], 3)[0]
        flux_vh_sc_list.append(flux_vh_sc)
        flux_sc_ve_list.append(flux_sc_ve)
        flux_ve_de_list.append(flux_ve_de)
        flux_de_receptor_list.append(flux_de_receptor)
        t_list.append(t_range[i])

        if np.all(np.fabs((flux_vh_sc - flux_sc_ve) / flux_vh_sc) < 1e-5):
            break
        # elif i == Nsteps-1 :
        #    raise ValueError('Simulation time too short to reach steady-state; re-run the simulation with longer time.')

        if disp >= 2:
            print('Time = ', t_range[i], 'Flux vh_sc= ', '{:.3e}'.format(flux_vh_sc), \
                  'Flux sc_down=', '{:.3e}'.format(flux_sc_ve))
        vehicle_conc = _skin.getComp(0, 0).getMeshConc()
        vehicle_conc_list.append(vehicle_conc[0])
        sc_conc = []
        for j in range(len(depth1_1)):
            sc_conc.append(_skin.getComp(1, 0).meshes[5+j*3*11].getConc())
        # if t_range[i] % 3600 == 0:
        sc_conc_list[:, i] = sc_conc
        ve_conc = _skin.getComp(2, 0).getMeshConc()
        # if t_range[i] % 3600 == 0:
        ve_conc_list[:, i] = ve_conc
        de_conc = _skin.getComp(3, 0).getMeshConc()
        # if t_radnge[i]%3600==0:
        de_conc_list[:, i] = de_conc
        mass[i, :] = _skin.compMass_comps()
        m_v[i, 0] = _skin.comps[0].getMass_OutEvap()
        total_mass_list.append(sum(_skin.compMass_comps()+m_v[i,0])/mass[0,0])
        # print('Vehicle conc =', _skin.getComp(1, 0).meshes[12].getConc())
        # Simulate
        _skin.solveMoL(t_range[i], t_range[i + 1])
    # flux_vh_sc: product from veicle to skin
    # flux_sc_down: product from sc down
    # plot flux against time
    if disp >= 1:
        print('MW= ', '{:.2f}'.format(_chem.mw), 'Flux vh_sc= ', '{:.3e}'.format(flux_vh_sc), \
              'Flux sc_down=', '{:.3e}'.format(flux_sc_ve))

    df = pd.DataFrame({'time': t_list, 'flux_vh_sc': flux_vh_sc_list, 'flux_sc_ve': flux_sc_ve_list, \
                       'flux_ve_de': flux_ve_de_list, 'flux_de_receptor': flux_de_receptor_list,\
                       # 'vehicle_conc': vehicle_conc_list, 'sc_conc': sc_conc_list, 've_conc': ve_conc_list,\
                       'evap':m_v/mass[0,0], 'mass0': mass[:,0]/mass[0,0], 'mass1': mass[:,1]/mass[0,0], \
                       'mass2': mass[:,2]/mass[0,0], 'mass3': mass[:,3]/mass[0,0], 'mass4': mass[:,4]/mass[0,0],\
                       'total_mass': total_mass_list})
            # Save fraction of mass in all compartments)
    
    
    # data = {
    #     'sc_conc': sc_conc_list[:,0]
    # }
    # df1 = pd.DataFrame(sc_conc_list)
    # df1.to_excel(wk_path + r'_sc_conc.xlsx')
    # df1 = pd.DataFrame(ve_conc_list)
    # df1.to_excel(wk_path + r'_ve_conc.xlsx')
    # df1 = pd.DataFrame(de_conc_list)
    # df1.to_excel(wk_path + r'_de_conc.xlsx')
    # df1 = pd.DataFrame(t_range[0:Nsteps-2])
    # df1.to_excel(wk_path + r'_t_range.xlsx')
    # df.to_excel(wk_path+r'_fluxAndMass.xlsx')
    depth1 = pd.DataFrame(depth1_1)
    # depth1.to_excel(wk_path + r'_sc_conc_dep.xlsx')
    depth2 = pd.DataFrame(depth2_2)
    # depth2.to_excel(wk_path + r'_ve_conc_dep.xlsx')
    depth3 = pd.DataFrame(depth3_3)
    # depth3.to_excel(wk_path + r'_de_conc_dep.xlsx')
    vehicle_conc = pd.DataFrame(vehicle_conc_list)
    sc_conc = pd.DataFrame(sc_conc_list)
    ve_conc = pd.DataFrame(ve_conc_list)
    de_conc = pd.DataFrame(de_conc_list)
    t_range = pd.DataFrame(t_range[0:Nsteps-2])
    return flux_vh_sc / _conf.init_conc_vh, df, depth1, depth2, depth3, vehicle_conc, sc_conc, ve_conc, de_conc, t_range
