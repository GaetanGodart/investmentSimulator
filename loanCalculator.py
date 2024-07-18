from matplotlib import pyplot as plt
import numpy as np

capital = 100000
durationInYear = [20, 25]   # has to be integer
interets  = [0.025, 0.05]

rmb = 0
InteretsPayes = np.array([0])
capitalPaye = np.array([0])
restantDu = np.array([100000])

fig, axs = plt.subplots(2, 2)

for interestRate in interets:
    for duration in durationInYear:
        
        mensualite = (interestRate/12*capital)/(1-(1/pow(1+interestRate/12, duration*12)))

        for i in range(duration*12+1):
            rmb = rmb + mensualite
            InteretsPayes = np.append(InteretsPayes, InteretsPayes[i]+restantDu[i]*interestRate/12)
            capitalPaye = np.append(capitalPaye, capitalPaye[i]+mensualite-restantDu[i]*interestRate/12)
            restantDu = np.append(restantDu, restantDu[i]-mensualite+restantDu[i]*interestRate/12)

        axs[interets.index(interestRate), durationInYear.index(duration)].plot(InteretsPayes+capitalPaye, label = "interets paye", color = 'red')
        axs[interets.index(interestRate), durationInYear.index(duration)].plot(capitalPaye, label = "capital paye", color = 'green')
        axs[interets.index(interestRate), durationInYear.index(duration)].fill_between(range(duration*12+2), InteretsPayes+capitalPaye, capitalPaye, color = 'red', alpha = .2)
        axs[interets.index(interestRate), durationInYear.index(duration)].fill_between(range(duration*12+2), capitalPaye, color = 'green', alpha = .2)
        axs[interets.index(interestRate), durationInYear.index(duration)].plot(restantDu, label = "restant du")
        axs[interets.index(interestRate), durationInYear.index(duration)].set_title(f"{capital/1000:.0f}k€ | {duration} years | {interestRate*100:.1f}% | {mensualite:.1f}€/month | {rmb/1000:.0f}k€ total")
        axs[interets.index(interestRate), durationInYear.index(duration)].legend()

        rmb = 0
        InteretsPayes = np.array([0])
        capitalPaye = np.array([0])
        restantDu = np.array([100000])


plt.show()