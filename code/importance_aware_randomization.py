import math
import numpy as np


def perturb(n, alpha, w, theta, mu,  score_array, epsilon, epsilon_reminded, sample_result):
    p = 1-math.exp(-(alpha/score_array[n]+(1-alpha)*score_array[n]))
    b = math.log(theta/score_array[n]+mu)
    epsilon_now = p*epsilon_reminded
    epsilon_reminded -= epsilon_now
    q = 0.5*epsilon_now/(1-math.exp(-epsilon_now*b))
    perturb_value = sample_function(q, epsilon_now)
    perturbed_result = sample_result[n]+perturb_value
    if epsilon_reminded>epsilon/2:
        alpha -= 1/(1-alpha)**2
    elif epsilon/w > epsilon_reminded:
        alpha += 1/(1-alpha)**2
    return alpha, perturbed_result, epsilon_reminded


def sample_function(a, b):
    number = np.random.random_sample()
    if np.random.random_sample()>0.5:
        return -1*math.log(b/a*(1-number))/b
    else:
        return 1*math.log(b/a*(1-number))/b
