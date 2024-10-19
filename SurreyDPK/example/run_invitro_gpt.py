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
    b_vary_vehicle = True
    b_inf_source = False

    _conf = config.Config(fn_conf)
    if sc_Kw_paras is not None:
        _conf.Kw_sc_paras = sc_Kw_paras
    if sc_D_paras is not None:
        _conf.D_sc_paras = sc_D_paras

    if chem is not None:
        _chem = chem
    else:
        _chem = chemical.Chemical(_conf)

    _skin = skin_setup.Skin_Setup(_chem, _conf)
    if infinite_vh:
        _skin.createComps(_chem, _conf, 'ZeroConc')
    else:
        _skin.createComps(_chem, _conf, 'ZeroFlux')

    t_start, t_end, Nsteps = [0, _conf.t_end, _conf.Nsteps]
    t_range = np.linspace(t_start, t_end, Nsteps)
    n_times = Nsteps - 1

    flux_vh_sc_list = []
    flux_sc_ve_list = []
    flux_ve_de_list = []
    flux_de_receptor_list = []
    vehicle_conc_list = []
    sc_conc_list = np.zeros([13, n_times])
    ve_conc_list = np.zeros([10, n_times])
    de_conc_list = np.zeros([10, n_times])
    total_mass_list = []
    nComps = _skin.nxComp * _skin.nyComp
    mass = np.zeros([n_times, nComps])
    t_list = []
    m_v_list = []

    depth1 = [
        7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08,
        4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07,
        7.5e-08,
        4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08, 4e-07, 4e-07, 7.5e-08
    ]
    depth1_1 = [sum(depth1[:i * 3 + 1]) for i in range(13)]
    depth2 = [1e-05] * 10
    depth2_2 = [sum(depth2[:i + 1]) for i in range(10)]
    depth3 = [2.94e-05] * 10
    depth3_3 = [sum(depth3[:i + 1]) for i in range(10)]

    for i in range(n_times):
        newpath = os.path.join(wk_path, str(t_range[i]))
        os.makedirs(newpath, exist_ok=True)

        if b_inf_source:
        	mass[0, :] = _skin.comps[0].getMass_OutEvap()
        	mass[i+1, :] = _skin.compMass_comps()
        	m_v = _skin.comps[0].getMass_OutEvap()
        	m_all = np.insert(mass, 0, m_v) / total_mass
        	total_mass_list.append(m_all)
        else:
        	mass[i, :] = _skin.compMass_comps()
        	evap = _skin.comps[0].getMass_OutEvap()
        	m_v = _skin.comps[0].getMass_OutEvap()
        	mass_evap = np.insert(mass, 0, m_v)
        	total_mass = np.sum(mass)
        	m_all = mass_evap / total_mass
        	total_mass_list.append(m_all)

        m_v_list.append(m_v)

        for j in range(nComps):
            fn = os.path.join(newpath, f'comp{j}_{_conf.comps_geom[j].name}')
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

        if disp >= 2:
            print(f'Time = {t_range[i]}, Flux vh_sc= {flux_vh_sc:.3e}, Flux sc_down= {flux_sc_ve:.3e}')

        vehicle_conc = _skin.getComp(0, 0).getMeshConc()
        vehicle_conc_list.append(vehicle_conc[0])
        sc_conc = [_skin.getComp(1, 0).meshes[5 + j * 3 * 11].getConc() for j in range(13)]
        sc_conc_list[:, i] = sc_conc
        ve_conc = _skin.getComp(2, 0).getMeshConc()
        ve_conc_list[:, i] = ve_conc
        de_conc = _skin.getComp(3, 0).getMeshConc()
        de_conc_list[:, i] = de_conc

        _skin.solveMoL(t_range[i], t_range[i + 1])
        full_mass = evap + mass[:, 0] +mass[:, 1]+mass[:, 2]+mass[:, 3]+mass[:, 4]
        
    if disp >= 1:
        print(f'MW= {_chem.mw:.2f}, Flux vh_sc= {flux_vh_sc:.3e}, Flux sc_down= {flux_sc_ve:.3e}')

    df = pd.DataFrame({
        'time': t_list,
        'flux_vh_sc': flux_vh_sc_list,
        'flux_sc_ve': flux_sc_ve_list,
        'flux_ve_de': flux_ve_de_list,
        'flux_de_receptor': flux_de_receptor_list,
        'evap': evap.any() / full_mass,
        'mass0': mass[:, 0] / full_mass,
        'mass1': mass[:, 1] / full_mass,
        'mass2': mass[:, 2] / full_mass,
        'mass3': mass[:, 3] / full_mass,
        'mass4': mass[:, 4] / full_mass,
        'total_mass': total_mass_list
    })

    return (
        flux_vh_sc / _conf.init_conc_vh,
        df,
        pd.DataFrame(depth1_1),
        pd.DataFrame(depth2_2),
        pd.DataFrame(depth3_3),
        pd.DataFrame(vehicle_conc_list),
        pd.DataFrame(sc_conc_list),
        pd.DataFrame(ve_conc_list),
        pd.DataFrame(de_conc_list),
        pd.DataFrame(t_range[0:Nsteps-2])
    )
