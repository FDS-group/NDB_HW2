import numpy as np
import matplotlib.pyplot as plt


def CDF_L_plot(alpha=1.882, b=20):
    x = np.arange(0, b, .01)
    F_L = (1-(1/(1+x)**alpha))/(1-(1/(1+b)**alpha))
    plt.plot(x, F_L)
    plt.vlines(x=1, ymax=1, ymin=0, linestyle='--')
    plt.show()


def CDF_inv_L(p, alpha=1.882, b=20):
    temp1 = 1 + (1/((1+b)**alpha))
    temp2 = 1/(1-p*temp1)
    res = (temp2**(1/alpha))-1
    return res


def sample_inter_arrival(lambda_, n=1000):
    unif = np.random.uniform(size=n)
    T = -np.log(unif)/lambda_
    return T


def sample_L(n=1000):
    unif = np.random.uniform(size=n)
    L = CDF_inv_L(unif)
    return L


CDF_L_plot()
print(sample_inter_arrival(lambda_=1, n=10))
print(sample_L(n=100))


CDF_inv_L(20)


# Basic Ideas and thoughts:
# - I think we have to assume that there is no Dispatching Delay, we will only focus on the server delay
# - "Identify the arrival processes at queue 1 and 2. Motivate your models.": First thought is that it should also
#   behave as a Poisson in both servers for any given \theta. The mean arrival time will be different from \Lambda but
#   the distribution is still the same. We probably have to show this using a simulation of the system to infer the new
#   poisson distribution for each server
# - "Identify the service time probability distributions at server 1 and server 2." Similarly to the previous point we
#   will also use simulation to find the distribution that X_1 and X_2 follow. In order to do this I guess we need to
#   take into consideration the number of tasks that arrive (we already have that info from before), the workload
#   distribution and finally the server capacity (which is given by the exercise).
# - "Write the expression of the mean delay E[D] through the two server cluster." Two hypothesis for this I think:
#       1. Mean delay is mean response time (so we have to sum over p_i*E[R_i] (see slide PS server farms)
#       2. Mean delay is the max between all E[R_i]
#   Regardless of the hypothesis we follow I think that the principle should be similar:
#       a. E[D] has to be a function of \theta and \Lambda
