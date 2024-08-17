import numpy as np

def calculateLoan(capital, duration, percentageFeeYearly, flatFeeMontly):
    costOfLoan = np.array([0])
    payedBack = np.array([0])
    remaining = np.array([capital])

    monthlyPayment = (percentageFeeYearly/100/12*capital) / (1-(1/pow(1+percentageFeeYearly/100/12, duration*12))) + flatFeeMontly

    for i in range(duration*12+1):
            costOfLoan = np.append(costOfLoan, costOfLoan[i] + remaining[i]*percentageFeeYearly/100/12 + flatFeeMontly*12)
            payedBack = np.append(payedBack, payedBack[i] + monthlyPayment - remaining[i]*percentageFeeYearly/100/12 - flatFeeMontly)
            remaining = np.append(remaining, remaining[i] - monthlyPayment + remaining[i]*percentageFeeYearly/100/12 + flatFeeMontly)

    return monthlyPayment, costOfLoan, payedBack, remaining