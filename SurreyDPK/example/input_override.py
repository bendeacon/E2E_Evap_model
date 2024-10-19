import tkinter as tk
import pandas as pd
import os

data = {
    'CHEM_MW': ['190'],
    'CHEM_KOW': ['0.8'],
    'Sc': ['0.2']
        }

df = pd.DataFrame(data, index=['Row0'])

# dictionary of properties
properties = {
    'Vehicle_thickness': '',
    'SC_thickness': '',
    'VE_thickness': '',
    'DE_thickness': '',
    'Sink_thickness': '',
    'CHEM_MW': '',
    'CHEM_KOW': '',
    'Sc':'',
    't_end': '',
    'Nsteps': ''
}

layers = {
    '0': 'Vehicle_thickness',
    '1': 'SC_thickness',
    '2': 'VE_thickness',
    '3': 'DE_thickness',
    '4': 'Sink_thickness'
}


currentpatn = os.path.abspath(__file__)
rootpath = os.path.dirname(currentpatn)
zz = rootpath + "\\config\\"
# read interested parameters from config
with open(zz + 'Caffeine_CE.cfg', 'r') as rf:
    for line in rf:
        line = line.split()
        if not line or line[0] == '#':
            continue
        if line[0] == 'COMP':
            layer = layers[line[1]]
            properties[layer] = line[2]
        elif line[0] == 'CHEM_MW':
            # calculated value has priority
            if 'CHEM_MW' in df.columns:
                properties['CHEM_MW'] = df.loc['Row0', 'CHEM_MW']
            else:
                properties['CHEM_MW'] = line[1]
        elif line[0] == 'CHEM_KOW':
            if 'CHEM_KOW' in df.columns:
                properties['CHEM_KOW'] = df.loc['Row0', 'CHEM_KOW']
            else:
                properties['CHEM_KOW'] = line[1]
        elif line[0] == 't_end':
            properties['t_end'] = line[1]
        elif line[0] == 'Nsteps':
            properties['Nsteps'] = line[1]


entries = []
root = tk.Tk()
root.title("Specify Key Chemical Properties")
cvs = tk.Canvas(root, width=500, height=600, relief='raised')
cvs.pack()
# GUI to view and modify parameters, and store them into the dataframe (df)
pointer = 50

loc = [100+i*75 for i in range(5)]


label = tk.Label(root, text='Properties values (numerical)')
label.config(font=('helvetica', 12))
cvs.create_window(250, pointer, window=label)

for i, property in enumerate(properties.keys()):

    D, R = i//5, i%5
    pointer = loc[R]
    label = tk.Label(root, text=property)
    label.config(font=('helvetica', 10))
    cvs.create_window(150+D*200, pointer, window=label)
    pointer += 25
    dv = tk.StringVar() # default value
    dv.set(properties[property])
    entry = tk.Entry(root, textvariable=dv)
    cvs.create_window(150+D*200, pointer, window=entry)
    entries.append(entry)
    # pointer += 50


def printer():
    for i, property in enumerate(properties.keys()):
        entry = entries[i]
        df.loc['Row0', property] = entry.get()
    root.destroy()

button = tk.Button(text='Submit & Continue', command=printer, font=('helvetica', 12))
cvs.create_window(250, loc[-1]+100, window=button)

root.mainloop()



print(df)
