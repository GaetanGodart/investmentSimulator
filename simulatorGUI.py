import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib import rcParams
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import numpy as np
from screeninfo import get_monitors

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

    capital = 100000
    duration = 20
    interestRate = 0.03
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
    canvas.get_tk_widget().pack()                       # placing the canvas on the Tkinter window 
    #toolbar = NavigationToolbar2Tk(canvas, window)      # creating the Matplotlib toolbar 
    #toolbar.update() 
    #canvas.get_tk_widget().pack()                       # placing the toolbar on the Tkinter window


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
        loanTab = ttk.Frame(master)
        self.master.add(loanTab, text = " Loan simulator ")
        plot(loanTab)


class StockSimulatorTab:
    def __init__(self, master):
        self.master = master
        stockTab = ttk.Frame(master)
        self.master.add(stockTab, text = " Stock simulator ")


# Main
def main():
    window = ttk.Window(themename = "darkly", title = "Investment simulator")                       # Themes : https://ttkbootstrap.readthedocs.io/en/latest/themes
    window.geometry(f"{m.width*0.8:.0f}x{m.height*0.8:.0f}+{m.width*0.1:.0f}+{m.height*0.1:.0f}")
    mainApp = MainApplication(window)
    window.mainloop()                                                                               # run the gui 


if __name__ == '__main__':
    main()