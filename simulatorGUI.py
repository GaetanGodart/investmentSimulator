import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from matplotlib import rcParams
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
import numpy as np

# Define colors
themeBackgroundColor = "#222222"
themeRed = "#d9534f"
themeGreen = "#5cb85c"

# Funcions
def plot():
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

    canvas = FigureCanvasTkAgg(fig, master = window)    # creating the Tkinter canvas containing the Matplotlib figure 
    canvas.draw() 
    canvas.get_tk_widget().pack()                       # placing the canvas on the Tkinter window 
    #toolbar = NavigationToolbar2Tk(canvas, window)      # creating the Matplotlib toolbar 
    #toolbar.update() 
    #canvas.get_tk_widget().pack()                       # placing the toolbar on the Tkinter window 

# Main
window = ttk.Window(themename="darkly")
window.title('Plotting in Tkinter')                                         # setting the title and  
window.geometry("500x500")                                                  # setting the dimensions of the main window 
plot()
window.mainloop()                                                           # run the gui 