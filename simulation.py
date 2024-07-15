#########################################################
#########################################################
###                                                   ###
###      Simulation comparant                         ###
###      1) Louer + investir en bourse                ###
###      2) Acheter + investir le reste               ###
###                                                   ###
#########################################################
#########################################################


###################
###   IMPORTS   ###
###################
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk


###################
###   DONNEES   ###
###################
# Global market
DUREE_SIMULATION = 20
INFLATION_MOYENNE = 1.03
CAPITAL_DEPART = 30000
SALAIRE_DISPO = 1500         # (2200 salary - 700 of expenses)
AUGMENTATION_SALAIRE_ANNEL = 1.05   # take in cosideration inflation ;)

# Bourse
revenuBourse = np.array([30000])
donneeBourse =   {"retourMoyenBrut" : 1.08,
                "taxes" : 0.172,
                "rent" : 1000}

# Location LMNP
revenusLMNP = np.array([30000])
DonneesLMNP =   {"rendementMoyen" : 5,
                "appreciationMoyenne" : 3,
                "impots" : 30,
                "tauxInteret" : 3.7,
                "taxeFonciere" : 900,
                "tauxNotaire" : 8,
                "assurance" : 100,
                "vacanceLocative" : 1}

# Location nue
revenusLocationNue = np.array([30000])
DonneesLocationNUe =    {"rendementMoyen" : 4,
                        "appreciationMoyenne" : 3,
                        "impots" : 30,
                        "tauxInteret" : 3.7,
                        "taxeFonciere" : 900,
                        "tauxNotaire" : 8,
                        "assurance" : 100,
                        "vacanceLocative" : 0.5}


#####################
###   FONCTIONS   ###
#####################
#
def calculateYearlyRent (annees):
    return 12*(donneeBourse["rent"]*pow(INFLATION_MOYENNE, annees))

#
def calculateYearlyAvailableSalary (annees):
    return 12*(SALAIRE_DISPO*pow(AUGMENTATION_SALAIRE_ANNEL, annees))

#
def display_table(array):
    root = tk.Tk()                                                              # Create the main window
    root.title("NumPy Array Table")
    frame = tk.Frame(root)                                                      # Create a frame for the Treeview and scrollbar
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Create the Treeview widget
    columns = [f"Year {i}" for i in range(array.shape[0])]
    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for col in columns: tree.heading(col, text=col)                             # Define the headings
    tree.insert("", "end", values=list(array))                                  # Insert data into the table

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)    # Attach a vertical scrollbar to the Treeview
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    root.mainloop()                                                             # Start the GUI event loop

#####################
###   MAIN LOOP   ###
#####################
for i in range(DUREE_SIMULATION):
    #revenuBourse = np.append(revenuBourse, (revenuBourse[i] + calculateYearlyAvailableSalary(i) - calculateYearlyRent(i)) * donneeBourse["retourMoyenBrut"])
    revenuBourse = np.append(revenuBourse, revenuBourse[i] * donneeBourse["retourMoyenBrut"])

#################
###   PRINT   ###
#################
revenuBourse = revenuBourse/1000           # get value in K

"""
plt.plot(revenuBourse)
#plt.yscale("log")                          # log scale
plt.ticklabel_format(scilimits=(-5, 8))    # prevent scientifica notation
plt.show()
"""

#display_table(revenuBourse)
print(f"{CAPITAL_DEPART} devient en {DUREE_SIMULATION} ans:\n - {revenuBourse[-1]:.2f}K brut\n - {revenuBourse[-1]*(1-donneeBourse["taxes"]):.2f}K net\n - {revenuBourse[-1]*(1-donneeBourse["taxes"])*(pow(0.97, DUREE_SIMULATION)):.2f}K net d'inflation")