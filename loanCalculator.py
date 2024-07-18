from matplotlib import pyplot as plt
import numpy as np

capital = 100000
durationInYear = 25
interets  = [0.015, 0.025, 0.035, 0.045]

rmb = np.array([0])
InteretsPayes = np.array([0])
capitalPaye = np.array([0])
restantDu = np.array([100000])

fig, axs = plt.subplots(2, 2)

for interestRate in interets:
        
    mensualite = (interestRate/12*capital)/(1-(1/pow(1+interestRate/12, durationInYear*12)))

    for i in range(durationInYear*12+1):
        rmb = np.append(rmb, rmb[i] + mensualite)
        InteretsPayes = np.append(InteretsPayes, InteretsPayes[i]+restantDu[i]*interestRate/12)
        capitalPaye = np.append(capitalPaye, capitalPaye[i]+mensualite-restantDu[i]*interestRate/12)
        restantDu = np.append(restantDu, restantDu[i]-mensualite+restantDu[i]*interestRate/12)

    if(interestRate == interets[0]): axis = axs[0, 0]
    elif(interestRate == interets[1]): axis = axs[0, 1]
    elif(interestRate == interets[2]): axis = axs[1, 0]
    else: axis = axs[1, 1]

    axis.plot(InteretsPayes+capitalPaye, label = "interets paye", color = 'red')
    axis.plot(capitalPaye, label = "capital paye", color = 'green')
    axis.fill_between(range(durationInYear*12+2), InteretsPayes+capitalPaye, capitalPaye, color = 'red', alpha = .2)
    axis.fill_between(range(durationInYear*12+2), capitalPaye, color = 'green', alpha = .2)
    axis.plot(restantDu, label = "restant du")
    axis.set_title(f"{capital/1000:.0f}k€ | {durationInYear} years | {interestRate*100:.1f}% | {mensualite:.1f}€/month | {(rmb[durationInYear*12+1])/1000:.0f}k€ total")
    axis.legend()

    rmb = np.array([0])
    InteretsPayes = np.array([0])
    capitalPaye = np.array([0])
    restantDu = np.array([100000])


plt.show()