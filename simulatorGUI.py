import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib import rcParams
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import numpy as np
from screeninfo import get_monitors


# Define colors
themeBackgroundColor = "#222222"
themeRed = "#d9534f"
themeGreen = "#5cb85c"


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

    rmb = 0
    capital = 100
    duration = 20
    interestRate = 0.03
    InteretsPayes = np.array([0])
    capitalPaye = np.array([0])
    restantDu = np.array([capital])
    mensualite = (interestRate/12*capital)/(1-(1/pow(1+interestRate/12, duration*12)))

    for i in range(duration*12+1):
        rmb = rmb + mensualite
        InteretsPayes = np.append(InteretsPayes, InteretsPayes[i]+restantDu[i]*interestRate/12)
        capitalPaye = np.append(capitalPaye, capitalPaye[i]+mensualite-restantDu[i]*interestRate/12)
        restantDu = np.append(restantDu, restantDu[i]-mensualite+restantDu[i]*interestRate/12)

    plot1.plot(InteretsPayes+capitalPaye, label = "interets paye", color = themeRed)                                    # Cost line
    plot1.plot(capitalPaye, label = "capital paye", color = themeGreen)                                                 # Capital line
    plot1.fill_between(range(duration*12+2), InteretsPayes+capitalPaye, capitalPaye, color = themeRed, alpha = .2)      # Cost area
    plot1.fill_between(range(duration*12+2), capitalPaye, color = themeGreen, alpha = .2)                               # Capital
    plot1.set_title(f"{duration} years | {interestRate*100:.1f}% | {mensualite:.2f}%/month | +{rmb-100:.0f}% payed")
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