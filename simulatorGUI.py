import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib import rcParams
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import numpy as np
from screeninfo import get_monitors
import re

# Local imports
import loanCalculator


# Define colors
themeBackgroundColor = "#222222"
themeRed = "#d9534f"
themeGreen = "#5cb85c"
themeBlue = "#375a7f"


# Set matplot theme colors
# To see all attributes : print( rcParams.keys())
rcParams['figure.facecolor'] = themeBackgroundColor
rcParams['legend.facecolor'] = themeBackgroundColor
rcParams['legend.labelcolor'] = "white"
rcParams['axes.edgecolor'] = "white"
rcParams['axes.labelcolor'] = "white"
rcParams['axes.facecolor'] = "white"
rcParams['ytick.labelcolor'] = "white"
rcParams['xtick.labelcolor'] = "white"
rcParams['ytick.color'] = "white"
rcParams['xtick.color'] = "white"
rcParams['text.color'] = "white"


for m in get_monitors():
    if(m.is_primary):
        monitorWidth = m.width
        monitorHeight = m.height
        break


# Funcions
def plot(destination):
    fig = Figure()                                      # the figure that will contain the plot 
    plot1 = fig.add_subplot(1, 1, 1)                    # adding the subplot 

    capital = 375000
    duration = 20
    interestRate = 0.025
    flatFee = 1.5

    montlyPayment, costOfLoan, payedBack, remaining = loanCalculator.calculateLoan(capital, duration, interestRate, flatFee)

    plot1.plot(costOfLoan + payedBack, label = "Cost of the loan", color = themeRed)                            # Cost line
    plot1.plot(payedBack, label = "Capital payed", color = themeGreen)                                          # Capital line
    plot1.plot(remaining, label = "Remaining", color = themeBlue)                                               # Remaining line
    plot1.fill_between(range(duration*12+2), costOfLoan + payedBack, payedBack, color = themeRed, alpha = .2)   # Cost area
    plot1.fill_between(range(duration*12+2), payedBack, color = themeGreen, alpha = .2)                         # Capital area
    plot1.set_title(f"{duration} years | {interestRate*100:.1f}% | {flatFee:.1f}€ flat | {montlyPayment:.0f}€/month | +{(100*costOfLoan[-1]+capital)/capital:.0f}% payed")
    plot1.legend()
    plot1.set_facecolor(themeBackgroundColor)

    canvas = FigureCanvasTkAgg(fig, master = destination)    # creating the Tkinter canvas containing the Matplotlib figure 
    canvas.draw() 
    canvas.get_tk_widget().pack()                            # placing the canvas on the Tkinter window 
    toolbar = NavigationToolbar2Tk(canvas, destination)      # creating the Matplotlib toolbar 
    toolbar.update() 
    canvas.get_tk_widget().pack()                            # placing the toolbar on the Tkinter window


class MainApplication:
    def __init__(self, master):
            self.master = master
            self.notebook = ttk.Notebook(master, width = monitorWidth, height = monitorHeight)
            self.notebook.pack()

            LoanSimulatorTab(self.notebook)
            StockSimulatorTab(self.notebook)   # later add "buyTab", "unfurnishedTab", "furnishedTab" and "setupTab"


class LoanSimulatorTab:
    def __init__(self, master):
        self.master = master
        self.digit_func = master.register(self.validate_number)
        self.padding = 5
        self.loanTab = ttk.Frame(master, padding = self.padding)
        self.master.add(self.loanTab, text = " Loan simulator ")
        self.loanTab.update()
        self.addSettingsFrame()
        self.addDisplayFrame()

    def addSettingsFrame(self):
        self.settingsFrame = ttk.Labelframe(self.loanTab, text='Setting', padding = 10)
        self.settingsFrame.pack(side = LEFT, fill = BOTH, expand = YES, padx = 5)
        # Plot button
        plotButton = ttk.Button(self.settingsFrame, text = "Generate loan simulation", command = lambda : self.plot())
        plotButton.pack(pady = 20)
        # Entry capiptal to lend
        capitalLabelFrame = ttk.LabelFrame(self.settingsFrame, text = "Capital to lend", padding = 10)
        capitalLabelFrame.pack(fill = None, expand = NO, pady = 10)
        capitalEntry = ttk.Entry(capitalLabelFrame, textvariable = "150000", validate="all", validatecommand=(self.digit_func, '%P'))    # Why no show 150000?
        capitalEntry.insert(0, "150000")
        capitalEntry.pack(padx = 20)
        # Entry duration of loan
        durationLabelFrame = ttk.LabelFrame(self.settingsFrame, text = "Duration of the loan (in years)", padding = 10)
        durationLabelFrame.pack(fill = None, expand = NO, pady = 10)
        durationEntry = ttk.Entry(durationLabelFrame, textvariable = "25", validate="all", validatecommand=(self.digit_func, '%P'))
        durationEntry.insert(0, "25")
        durationEntry.pack(padx = 20)
        # Entry interest rate per year
        interestLabelFrame = ttk.LabelFrame(self.settingsFrame, text = "Interest rate (per year)", padding = 10)
        interestLabelFrame.pack(fill = None, expand = NO, pady = 10)
        interestEntry = ttk.Entry(interestLabelFrame, textvariable = "0.03", validate="all", validatecommand=(self.digit_func, '%P'))
        interestEntry.insert(0, "0.03")
        interestEntry.pack(padx = 20)
        # Entry flat fee per month
        flatFeeLabelFrame = ttk.LabelFrame(self.settingsFrame, text = "Flat fee (per month)", padding = 10)
        flatFeeLabelFrame.pack(fill = None, expand = NO, pady = 10)
        flatFeeEntry = ttk.Entry(flatFeeLabelFrame, textvariable = "1.5", validate="all", validatecommand=(self.digit_func, '%P'))
        flatFeeEntry.insert(0, "1.5")
        flatFeeEntry.pack(padx = 20)

    def addDisplayFrame(self):
        displayWindow = self.DisplayFrame = ttk.Labelframe(self.loanTab, text='Display', padding = 10)
        self.DisplayFrame.pack(side = RIGHT, fill = BOTH, expand = YES, padx = 5)
        plot(self.DisplayFrame)

    def validate_number(self, s) -> bool:
        cleaned = s.replace(' ', '').replace(',', '.')              # Remove spaces and replace commas with dots
        if re.match(r'^[+-]?(\d+(\.\d*)?|\.\d+)$', cleaned):  return True     # Use regular expression to ensure there is only one decimal point
        return False
    
    def plot(self):
        print("Called plot")


class StockSimulatorTab:
    def __init__(self, master):
        self.master = master
        stockTab = ttk.Frame(master)
        self.master.add(stockTab, text = " Stock simulator ")


# Main
if __name__ == '__main__':
    window = ttk.Window(themename = "darkly", title = "Investment simulator")                       # Themes : https://ttkbootstrap.readthedocs.io/en/latest/themes
    window.geometry(f"{m.width*0.8:.0f}x{m.height*0.8:.0f}+{m.width*0.1:.0f}+{m.height*0.1:.0f}")
    mainApp = MainApplication(window)
    window.mainloop()
    