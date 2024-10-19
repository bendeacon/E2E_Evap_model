import tkinter as tk
import pandas as pd

root = tk.Tk()
root.title("Specify Key Chemical Properties")

cvs = tk.Canvas(root, width=400, height=700, relief='raised')
cvs.pack()

data = {
    'Vehicle_thickness': [''],
    'SC_thickness': [''],
    'VE_thickness': [''],
    'DE_thickness': [''],
    'Sink_thickness': [''],
    'CHEM_MW': [''],
    'CHEM_KOW': [''],
}

df = pd.DataFrame(data, index=['values'])
entries = []

# Description
pointer = 25
for i in range(len(df.columns)+1):
    if i==0:
        label = tk.Label(root, text='Properties values (numerical)')
        label.config(font=('helvetica', 12))
        cvs.create_window(200, pointer, window=label)
        pointer += 50
    else:
        property = df.columns[i-1]
        label = tk.Label(root, text=property)
        label.config(font=('helvetica', 10))
        cvs.create_window(200, pointer, window=label)
        pointer += 25
        entry = tk.Entry(root)
        cvs.create_window(200, pointer, window=entry)
        entries.append(entry)
        pointer += 50

def printer():
    for i in range(len(entries)):
        entry = entries[i]
        property = df.columns[i]
        df.loc['values', property] = entry.get()
    root.destroy()

button = tk.Button(text='Submit & Continue', command=printer, font=('helvetica', 12))
cvs.create_window(200, pointer, window=button)

root.mainloop()

print(df)


